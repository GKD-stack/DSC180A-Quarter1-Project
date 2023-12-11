# imports
import pandas as pd
import os
import pandas_plink as pp
import statsmodels.api as sm

# main directory
main_dir = os.getcwd()[:-3]

# load gene expression data
gene_expression_data = pd.read_csv(main_dir + "data/gene_expression.txt", delimiter = "\t")

# slice the string to make the gene symbols consistent with gene_annotation data
gene_expression_data['TargetID'] = gene_expression_data['TargetID'].str.split('.').str[0]
gene_expression_data['Gene_Symbol'] = gene_expression_data['Gene_Symbol'].str.split('.').str[0]

# load gene annotation data
gene_annotation_data = pd.read_csv(main_dir + "data/gene_annotation.txt", delimiter = "\t")

# Filter for protein-coding genes
protein_coding_genes = gene_annotation_data[gene_annotation_data['TYPE'] == 'protein_coding']

# Get a list of protein-coding gene symbols
protein_coding_symbols = protein_coding_genes['SYM'].tolist()

# Subset gene_expression_data for protein-coding genes
protein_coding_expression_data = gene_expression_data[gene_expression_data['Gene_Symbol'].isin(protein_coding_symbols)]


# Method that will run the eQTL analysis for an intended chromosome
def eQTL(chromosome):

    # Filters gene expression and annotation data to only intended chromosome
    expression_data = protein_coding_expression_data[protein_coding_expression_data['Chr'] == str(chromosome)]
    gene_annot = gene_annotation_data[gene_annotation_data['CHR'] == chromosome]

    # Read plink files
    (bim, fam, bed) = pp.read_plink(main_dir + 'data/LDREF/1000G.EUR.' + str(chromosome))

    # Find common individuals
    fam_ids = fam['fid'].tolist()
    expression_ids = expression_data.columns.tolist()
    intersection_ids = set(fam_ids).intersection(set(expression_ids))
    intersection_ids_list = list(intersection_ids)

    # Filter the expression data and genotype data to include only common individuals
    expression_data_filtered = expression_data[intersection_ids_list]
    bed_filtered = bed[:, fam[fam['fid'].isin(intersection_ids_list)].index].compute()


    # Cis-eQTL Analysis ####################################################

    results = []
    window_size = 500000  # 500 Kb window size

    for gene_row in gene_annot.itertuples():
        gene_id = gene_row.ID
        gene_sym = gene_annot[gene_annot["ID"] == gene_id]["SYM"].iloc[0]
        gene_start = gene_row.START
        gene_end = gene_row.STOP

        # Filter SNPs within the window of the gene
        cis_snps = bim[(bim['pos'] > gene_start - window_size) & (bim['pos'] < gene_end + window_size)]

        if cis_snps.empty:
            continue
        gene_expression_df = expression_data_filtered[expression_data["TargetID"] == gene_sym]

        if gene_expression_df.empty:
            continue

        gene_expression = gene_expression_df.iloc[0]

        for snp_row in cis_snps.itertuples():
            snp_id = snp_row.snp
            snp = bed_filtered[snp_row.Index, :]

            if len(gene_expression) != len(snp):
                # Handle mismatch in length between gene expression and SNP data
                continue

            # Add a constant term to the independent variables to represent the intercept
            snp_with_intercept = sm.add_constant(snp)

            # Perform linear regression
            model = sm.OLS(gene_expression, snp_with_intercept)
            result = model.fit()

            # Check if there are enough parameters in the results
            if len(result.params) < 2:
                continue

            pvalue = result.pvalues[1]
            beta = result.params[1]
            std_err = result.bse[1]

            results.append({
                'gene_id': gene_id,
                'gene_symbol': gene_sym,
                'snp_id': snp_id,
                'pvalue': pvalue,
                'OR': beta,
                'SE': std_err,
                'snp_position': snp_row.pos
            })

    return results


# DataFrame to store results
all_results = pd.DataFrame()

# Runs the eQTL analysis for all the chromosomes
for chromosome in range(1,23):
    result = eQTL(chromosome)

    # Concatenates into one dataset
    all_results = pd.concat([all_results] + [pd.DataFrame([res]) for res in result], ignore_index=True)

    print("Finished eQTL Analysis for " + str(chromosome))
print("Finished all Analyses")

# Save results
all_results.to_csv(main_dir + "results/eQTL_result.txt", sep = "\t")

# Filters dataset and saves only significant results
all_results_sig = all_results[all_results["pvalue"] < 0.01]

# Adding absolute value of beta inorder to be able to sort
all_results_sig["abs_OR"] = all_results_sig["OR"].abs()

# Sorting by most significant results
all_results_sig = all_results_sig.sort_values(by=['pvalue', 'abs_OR'], ascending=[True, False])

# Saving results of most significant
all_results_sig.to_csv(main_dir + "results/eQTL_result_sig.txt", sep = "\t")

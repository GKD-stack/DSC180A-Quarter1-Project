#prepare summary statistics for prs generation
prepare_summary_stats_for_prs("alz_data.txt", ['SNP', 'A1', 'BETA'], "alz_data.gwas.txt")
prepare_summary_stats_for_prs("megastroke.txt", ['MarkerName', 'Allele1', 'Effect'], "megastroke.gwas.txt")
prepare_summary_stats_for_prs(input_file_name, ['rs_number', 'reference_allele', 'beta'], "bone.gwas.txt")

#save graphs and return percentile scores
alz_percentile = plot_prs_dist("prs_for_alz", "Alzheimer's Disease")
mgs_percentile = plot_prs_dist("prs_for_mgs", "Mega Stroke")
bone_percentile = plot_prs_dist("prs_for_bone", "Bone Density and Fracture")
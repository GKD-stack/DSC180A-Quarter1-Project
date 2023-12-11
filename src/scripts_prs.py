# Imports
import matplotlib.pyplot as plt
import seaborn as sns
import os
from scipy import stats
import pandas as pd


# main directory
main_dir = os.getcwd()[:-3]


# Read in the GWAS summary statistics and rename them to fit stats
def prepare_summary_stats_for_prs(input_file_name, input_columns, output_file_name):
  """
  input_file_name: Height.gwas.txt
  input_columns: These are the columns that represent SNP, ALLELE, BETA in your specific file
  ex) ['SNP', 'A1', 'OR']
  output_file_name: Height.formatted.gwas.txt
  """
  gwas_summary = pd.read_csv(f'{input_file_name}', sep='\t')
  prs_data = gwas_summary[input_columns].copy()
  prs_data.columns = ['SNP', 'ALLELE', 'BETA']
  prs_data['ALLELE'] = prs_data['ALLELE'].str.upper()
  prs_data.to_csv(f'{output_file_name}', sep=' ', index=False)
    

# Method for making PRS plots
def plot_prs_dist(file_name, trait, person):
    
    prs_data = pd.read_csv(main_dir + "data/profiles/" + file_name + ".profile", delim_whitespace=True)
    
    # plot the distribution
    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 6))
    sns.histplot(prs_data['SCORE'], kde=True, color="skyblue", bins=30)
    plt.title(f'Distribution of PRS for {trait}')
    plt.xlabel('Polygenic Risk Score')
    plt.ylabel('Frequency')

    # plot line for the person of interest
    person_prs = prs_data[prs_data['IID'] == person]['SCORE'].iloc[0]
    plt.axvline(person_prs, color='red', linestyle='dashed', linewidth=2)
    plt.text(person_prs, plt.ylim()[1]*0.9, person, color = 'red')

    # Shows graph
    plt.legend(['1KG Individuals', person])
    plt.show()

    # Returns percentile from distribution for person of interest
    percentile = stats.percentileofscore(prs_data['SCORE'], person_prs)
    print(person + " falls in the " + str(percentile) + " percentile")


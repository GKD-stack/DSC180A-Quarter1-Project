

def plot_prs_dist(prfile_file_name, trait):
"""
prfile_file_name: This is the name of the profile file without the extension. 
ex) prs_for_mgs

trait: The name of the trait
ex) Mega Stroke
"""
  prs_data = pd.read_csv(f'{prfile_file_name}.profile', delim_whitespace=True)
  prs_data.head()
  # plot the distribution
  sns.set(style="whitegrid")
  plt.figure(figsize=(10, 6))
  sns.histplot(prs_data['SCORE'], kde=True, color="skyblue", bins=30)
  plt.title(f'Distribution of PRS for {trait}')
  plt.xlabel('Polygenic Risk Score')
  plt.ylabel('Frequency')

  tiffany_prs = prs_data[prs_data['IID'] == 'Tiffany']['SCORE'].iloc[0]
  plt.axvline(tiffany_prs, color='red', linestyle='dashed', linewidth=2)
  plt.text(tiffany_prs, plt.ylim()[1]*0.9, 'Tiffany', color = 'red')

  # Show
  plt.legend(['1KG Individuals', 'Tiffany'])
  plt.show()

  from scipy import stats
  tiffany_prs = prs_data[prs_data['IID'] == 'Tiffany']['SCORE'].iloc[0]
  percentile = stats.percentileofscore(prs_data['SCORE'], tiffany_prs)
  print(percentile)
  return percentile 

def prepare_summary_stats_for_prs(input_file_name, output_file_name):
  """
  input_file_name: Height.gwas.txt
  output_file_name: Height.formatted.gwas.txt
  """
  gwas_summary = pd.read_csv(f'{input_file_name}', sep='\t')
  prs_data = gwas_summary[['SNP', 'A1', 'OR']].copy()
  prs_data.columns = ['SNP', 'ALLELE', 'BETA']
  prs_data['ALLELE'] = prs_data['ALLELE'].str.upper()
  prs_data.to_csv(f'{output_file_name}', sep=' ', index=False)

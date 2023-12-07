# Genetic Risk Prediction Capstone Project

## Introduction

This capstone project, part of the Data Science Capstone Domain of Inquiry (DSC 180AB A17 2022-2023), focuses on the genetic risk prediction of gene expression, complex traits, and polygenic diseases. Developed by Tiffany Amariuta, this project explores the utility of polygenic risk scores (PRS) in assessing an individual's genetic predisposition to various phenotypes.

## Project Description

Polygenic Risk Scores (PRS) are calculated as a weighted sum of an individual's genetic variants, offering a quantitative measure of genetic liability to a given phenotype. These scores are constructed using genome-wide association study (GWAS) data for complex traits or diseases, or expression quantitative trait loci (eQTL) data for gene expression.

The project aims to unravel the genetic architecture underlying disease phenotypes and their expression patterns, addressing questions of genetic variation propagation through gene expression, correlations between genetic liabilities, and the elusive factors contributing to phenotypic variance.

More Specifically, the project is as follows: 
1. Identifying cis-eQTLs in 1000 Genomes LCLs
2. Predicting Genetic Risk for Different Diseases in the 1000G Individuals and Plot the Professor's data on the Distribution. 


## Analysis Overview

The following analyses form the core of this capstone project:

- **eQTL Analysis**: Detection of genetic effects on gene expression.
- **Colocalization Analysis**: Identification of disease-associated genes through eQTL and GWAS data integration.
- **Fine-Mapping Analysis**: Determining causative variants from the detected eQTLs.

## Tools and Languages

For the analyses, Python was the primary programming language used due to its flexibility, extensive libraries for data analysis, and ease of sharing via collaborative platforms such as Google Colab.
Plink2 was used significantly for manipulating genetic data and generating polygenic risk scores. Significant coding for this project started during week 3 of the quarter. Prior to that, we set up 
Plink2 on our local systems and got familier with the existing literature. Software dependencies needed to run the code are accounted for in each notebook.

## Data Description

The data employed in this project includes:

- **Chromosomal Data (LDREF Folder)**: Contains BED, BIN, and FAM files for all chromosomes, facilitating the analysis of genotype data.
- **Frequency File**: Accompanies the chromosomal data, providing allele frequency information.
- **Expression Data (`expression.txt`)**: Contains transcriptomic data used for eQTL analysis.
- **Polygenic Risk Scores for Diseases (`prs_for_bone.profile, prs_for_alz.profile, prs_for_mgs.profile`)**: Contains the PRS for each individual and the professor for that particular disease. 

## Running the Analysis

To run the analysis and reproduce the results, follow these steps:

### Prerequisites

Ensure you have the following installed:
- Python (version 3.7 or later)
- Required Python libraries: `pandas_plink`, `statsmodels`, `numpy`, `pandas`, `matplotlib`
- PLINK 2.0 (for manipulating genetic data)

### Data Setup

1. Download the required data files:
   - `GD462.GeneQuantRPKM.50FN.samplename.resk10.txt` (Gene expression data)
   - `gene_annot.txt` (Gene annotation data)
   - Chromosomal data files (`1000G.EUR.[chromosome number].bed`, `.bim`, `.fam`) for all chromosomes from the LDREF folder

2. Place these files in a known directory on your local machine.

### Running the Code

1. Open a Python environment where you have installed the necessary libraries.

2. Execute the provided Jupyter Notebook "Lihao_Liu_DSC180A_1000_Genomes". The notebook includes steps for:
   - Reading and preprocessing the gene expression and annotation data.
   - Conducting eQTL analysis for each chromosome.
   - Compiling the results into a comprehensive dataset.
   - Saving the results to local folder
   - Filtering significant SNPs based on a certain p-value

   Here is an example snippet to get you started:
   
   ```python
   import pandas as pd
   import pandas_plink as pp
   # ... other imports ...

   # Read gene expression data
   gene_expression_data = pd.read_csv('path/to/GD462.GeneQuantRPKM.50FN.samplename.resk10.txt', delimiter='\t')
   # ... further steps ...

   # eQTL analysis for each chromosome
   # ... code for eQTL analysis ...

## Clean this part up but just a start on my end


Other supplemental data was added as needed for each assignment. 

## Contributions

The quarter 1 project an application of all the skills we had learned each week. For the checkpoint, all the code was written by Gurman Dhaliwal. For the final project, Gurman did part 2 of the coding, started and cleaned the LaTeX template, and wrote the majority of the introduction, literature review, and the parts corresponding to part 2 of the project in project goals, methodology, results, and the conclusion. Lihao Liu completed part 1 of the coding, and did substantive editing to the final report, LaTeX formatting, and writing which included half of the project goals, methodology, and results. 

# Genetic Risk Prediction Capstone Project

## Introduction

This capstone project, part of the Data Science Capstone Domain of Inquiry (DSC 180AB A02), focuses on the genetic risk prediction of gene expression, complex traits, and polygenic diseases. Developed by Tiffany Amariuta, this project explores the utility of polygenic risk scores (PRS) in assessing an individual's genetic predisposition to various phenotypes.

## Project Description

Polygenic Risk Scores (PRS) are calculated as a weighted sum of an individual's genetic variants, offering a quantitative measure of genetic liability to a given phenotype. These scores are constructed using genome-wide association study (GWAS) data for complex traits or diseases, or expression quantitative trait loci (eQTL) data for gene expression.

The project aims to unravel the genetic architecture underlying disease phenotypes and their expression patterns, addressing questions of genetic variation propagation through gene expression, correlations between genetic liabilities, and the elusive factors contributing to phenotypic variance.

More specifically, the project is as follows: 
1. Identifying cis-eQTLs in 1000 Genomes LCLs
2. Predicting Genetic Risk for Different Diseases in the 1000G Individuals and Plot the Professor's Data on the Distribution. 


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
- **Expression Data (`gene_expression.txt`)**: Contains transcriptomic data used for eQTL analysis.
- **Polygenic Risk Scores for Diseases (`prs_for_bone.profile, prs_for_alz.profile, prs_for_mgs.profile`)**: Contains the PRS for each individual and the professor for that particular disease.
- **Preprocessed Summary Statistics Files for Diseases (bone.txt (https://drive.google.com/file/d/1Jd_vY8_pcI4pynkxjww4wAjati1aNsC-/view?usp=sharing), alz_data.txt (https://drive.google.com/file/d/1EL6ubS50S2MWTDKP1vLTQuvWQFpplYKk/view?usp=sharing), megastroke.txt (https://drive.google.com/file/d/13MnzxAV51hg0tY1nUK3-nT9UfQmI6u5X/view?usp=sharing))**: These files were too large to upload to GitHub. You can download them from the Google Drive links.

## Running the Analysis

To run the analysis and reproduce the results, follow these steps:

### Prerequisites

Ensure you have the following installed:
- Python (version 3.7 or later)
- Required Python libraries: `pandas_plink`, `statsmodels`, `os`, `pandas`, `matplotlib`, `seaborn`, `scipy`
- PLINK 2.0 (for manipulating genetic data)
- (optional) bcftools (if you are going to include your own data)
- Software that can unzip files (like winrar or 7-zip)

### Data Setup

1. Download this repository

2. Open the `data` folder and unzip the `gene_expression.zip`. Save the `gene_expression.txt` file in that same directory

3. Download these three files from Google drive
   - bone.txt (https://drive.google.com/file/d/1Jd_vY8_pcI4pynkxjww4wAjati1aNsC-/view?usp=sharing)
   - alz_data.txt (https://drive.google.com/file/d/1EL6ubS50S2MWTDKP1vLTQuvWQFpplYKk/view?usp=sharing)
   - megastroke.txt (https://drive.google.com/file/d/13MnzxAV51hg0tY1nUK3-nT9UfQmI6u5X/view?usp=sharing)

4. Place these three files in the `data` folder
   
### Running the Code

1. Execute the Python file `part1_eQTL_analysis.py` This file is responsible for:
   - Reading and preprocessing the gene expression and annotation data
   - Conducting eQTL analysis for each chromosome
   - Compiling the results into a comprehensive dataset
   - Saving the results to the `results` folder
   - Filtering significant SNPs based on a certain p-value
   
   results of running this Python file:
   - file `eQTL_results.txt` in the `results` folder containing the full resulting dataset from the eQTL analysis
   - file `eQTL_results.sig.txt` in the `results` folder containing only the significant values that we analyzed in our report  
   
2. Open the Jupyter notebook "part2_PRS.ipynb" and run all the cells, our specific analysis results are located under the "Our Analysis" section. Provided in this document are:
    - Our steps and additional instructions for replicating our analysis with different data
    - PRS Analysis for several diseases and genetic predispositions for our mentor

   results of running this Jupyter notebook file:
   - file `alz_data.gwas.txt` in the `results` folder containing the cleaned GWAS data for Alzheimer's disease
   - file `bone.gwas.txt` in the `results` folder containing the cleaned GWAS data for Bone density and fracture
   - file `megastroke.gwas.txt` in the `results` folder containin the cleaned GWAS data for Mega stroke

For this section, you could also run these commands from your Command Prompt. 
1. **Install Required Packages**:
   Run the following command to install the necessary Python packages from the `requirements.txt` file:
 `pip install -r src/requirements.txt`
2. **Run the analysis**
  Run the following command to generate the processed summary statistics files with the .gwas extension, which you can use with the plink commands provided in the analysis part 2 notebook for futher analysis. 
 `python src/run.py`
Check the results folder. 


## Repository Layout

**data** (contains our data files)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**LDREF** (Chromosomal data for 1000G individuals)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**profiles** (Polygenic Risk Scores for selected Diseases)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**prs_for_alz.profile** (PRS for Alzheimer's Disease)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**prs_for_bone.profile** (PRS for Bone Density and Fracture)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**prs_for_mgs.profile** (PRS for Mega Stroke)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**gene_annoation.txt** (gene annotation data)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**gene_expression.zip** (gene expression data in a zip file)  
    
**results** (contains code results from our analysis)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**alz_data.gwas.txt** (Cleaned Alzheimer's disease GWAS data)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**bone.gwas.txt** (Cleaned Bone Density and Fracture GWAS data)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**eQTL_result.txt** (Full result from eQTL analysis)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**eQTL_result_sig.txt** (Significant results from eQTL analysis)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**megastroke.gwas.txt** (Cleaned Mega Stroke GWAS data)

**src** (contains our code and scripts)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**part1_eQTL_analysis.py** (Runs the eQTL analysis for 1000G individuals)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**part2_PRS.ipynb** (Instructions and results for our PRS analysis)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**scripts_prs.py** (Scripts and methods used to conduct PRS analysis)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**requirements.txt** (The required packages for Part 2 of the project)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**run.py** (The executable script to generating the prepared summary statistics for PLINK)  

**README.md** (Information on repository)  


## Contributions

The quarter 1 project was an application of all the skills we had learned each week. For the checkpoint, all the code was written by Gurman Dhaliwal. For the final project, Gurman did part 2 of the coding, started and cleaned the LaTeX template, and wrote the majority of the introduction, literature review, and the parts corresponding to part 2 of the project in project goals, methodology, results, and conclusion. Lihao Liu completed part 1 of the coding and did substantive editing to the final report, LaTeX formatting, and writing which included half of the project goals, methodology, and results. Anton Beliakov organized and structured the repository, rewrote the code to make our analysis reproducible, and assisted in the writing of the introduction, writing, and organization of the literature review as well as general report and code editing.

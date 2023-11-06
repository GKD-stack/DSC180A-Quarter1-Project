# Genetic Risk Prediction Capstone Project

## Introduction

This capstone project, part of the Data Science Capstone Domain of Inquiry (DSC 180AB A17 2022-2023), focuses on the genetic risk prediction of gene expression, complex traits, and polygenic diseases. Developed by Tiffany Amariuta, this project explores the utility of polygenic risk scores (PRS) in assessing an individual's genetic predisposition to various phenotypes.

## Project Description

Polygenic Risk Scores (PRS) are calculated as a weighted sum of an individual's genetic variants, offering a quantitative measure of genetic liability to a given phenotype. These scores are constructed using genome-wide association study (GWAS) data for complex traits or diseases, or expression quantitative trait loci (eQTL) data for gene expression.

The project aims to unravel the genetic architecture underlying disease phenotypes and their expression patterns, addressing questions of genetic variation propagation through gene expression, correlations between genetic liabilities, and the elusive factors contributing to phenotypic variance.

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

Other supplemental data was added as needed for each assignment. 

## Contributions

The project began with individual contributions from students. The checkpoint written report also started out as individual efforts, but it 
turned into a collaborative effort, consolidating the findings and insights gained throughout the project. 
All coding tasks in this repository were independently completed by Gurman Dhaliwal. 

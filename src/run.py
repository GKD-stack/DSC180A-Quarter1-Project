#!/usr/bin/env python

import sys
import json
import scripts_prs as prs

def main(targets):
    if 'data' in targets:
        with open('data-params.json') as fh:
            data_params = json.load(fh)
        get_data(**data_params)

    if 'prepare_alz' in targets:
        prs.prepare_summary_stats_for_prs("alz_data.txt", ['SNP', 'A1', 'BETA'], "alz_data.gwas.txt", " ")

    if 'prepare_megastroke' in targets:
        prs.prepare_summary_stats_for_prs("megastroke.txt", ['MarkerName', 'Allele1', 'Effect'], "megastroke.gwas.txt", " ")

    if 'prepare_bone' in targets:
        prs.prepare_summary_stats_for_prs("bone.txt", ['rs_number', 'reference_allele', 'beta'], "bone.gwas.txt", " ")

    if 'plot_prs' in targets:
        prs.plot_prs_dist("prs_for_alz", "Alzheimer's Disease", "Tiffany")
        prs.plot_prs_dist("prs_for_mgs", "Mega Stroke", "Tiffany")
        prs.plot_prs_dist("prs_for_bone", "Bone Density and Fracture", "Tiffany")

if __name__ == '__main__':
    targets = sys.argv[1:]
    main(targets)

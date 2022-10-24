#!/usr/bin/env python3
import pyranges as pr
import sys
import pandas as pd

def parse_vcf(vcf_file):

    chromosome_list = []
    start = []
    end = []
    snp_data = []
    ref_list = []
    alt_list = []
    snp_type = []
    #vcf_file = sys.argv[1]
    with open(vcf_file, 'r') as vcf_file:
        for line in vcf_file:
            line = line.rstrip()
            if line.startswith('##'):
                continue
            if line.startswith('#'):
                continue
            else:
                chromosome, position, ID, REF, ALT, QUAL, thirdthing, types = (line.split('\t'))
                chromosome_list.append(chromosome)
                start.append(position)
                end.append(position)
                ref_list.append(REF)
                alt_list.append(ALT)
                snp_type.append(types)
                snp_data.append((REF.upper()+' ' +ALT.upper()+' ' +types))

                test_dictionary = {"Chromosome": chromosome_list, "Start" : start, "End" : end, "Ref" : ref_list, "Alt": alt_list, "SNPtype": snp_type}
                pyranges_df = pr.from_dict(test_dictionary)
                vcf_df = pyranges_df.as_df()
                return vcf_df

def main():
    vcf_file=sys.argv[1]
    vcf_df=parse_vcf(vcf_file)
    return vcf_df
    print(vcf_df) 

if __name__=='__main__':
    main()

#!/usr/bin/env python3
import pyranges as pr
import sys

vcf_in = 'output.vcf'

def vcfpy(vcf_in):
    chromosome_list = []
    start = []
    end = []
    snp_data = []
    ref_list = []
    alt_list = []
    snp_type = []
    with open(vcf_in, 'r') as vcf_file:
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

#test_dictionary = {"Chromosome": chromosome_list}
    test_dictionary = {"Chromosome": chromosome_list, "Start" : start, "End" : end, "Ref" : ref_list, "Alt": alt_list, "SNPtype": snp_type}
    df = pr.from_dict(test_dictionary)
    #print(df)
    insertion_subset = (df.SNPtype == "TYPE=INSERT")
    indel_subset = (df.SNPtype == ("TYPE=DELETE" and "TYPE=INSERT"))
    substitute_subset = (df.SNPtype == "TYPE=SUBSTITUTE")
    print(df['Start'])
    with open('./output/df.txt', 'w') as data:
        data.write(str(df))
vcfpy(vcf_in)    

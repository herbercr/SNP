#!/usr/bin/env python3

#from SNP import aignment
output = 'output.vcf'

def vcfdict(output): 
    list_of_snps = []
    dictionary_of_snps = {}
    output = 'output.vcf'
    with open(output, 'r') as vcf_file:
        for line in vcf_file:
            line = line.rstrip()
            if line.startswith('##'):
                continue
            if line.startswith('#'):
                continue
            else:
                chromosome, position, ID, REF, ALT, QUAL, thirdthing, types = (line.split('\t'))
                if chromosome not in dictionary_of_snps:
                    dictionary_of_snps[chromosome] = {}
                if position not in dictionary_of_snps[chromosome]:
                    dictionary_of_snps[chromosome][position] = [REF, ALT, types]
    print(dictionary_of_snps)
vcfdict(output)

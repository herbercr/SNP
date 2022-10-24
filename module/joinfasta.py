#!/usr/bin/env python3

import sys, re

test = 'test.fasta'
def join(test):
    fasta_p = {} #starts with fasta parser
    #fasta = sys.argv[1] #input from sys
    with open(test, 'r') as fasta:
        for line in fasta:
	        line = line.rstrip()
	        if line.startswith(">"):    
		        gene = line.lstrip(">") #chooses gene ID
	        else:
		        seqn = line #chooses seqn lines
		        fasta_p[gene] = seqn    #dict containing gene IDs as keys and seqns as values
    for k, v in fasta_p.items():
    	print(v)

    fasta_seqns_list = list(fasta_p.values())
    #print(fasta_seqns_list)

    DNA_seqn = ''
    DNA_seqn = ''.join(fasta_seqns_list)

    #print(DNA_seqn)

    w = open('final_fasta.fasta', 'w')
    w.write(DNA_seqn)
    w.close()

    codon_start = 1
    codons = re.findall(r"(.{3})", DNA_seqn)
    #print(codons)
    snp_pos = 9
    for index,codon in enumerate (codons):
        codon_end = codon_start + 2
        if codon_start <= snp_pos <= codon_end:
            print(codon,index,codon_start,codon_end)
        codon_start += 3
    join(test)

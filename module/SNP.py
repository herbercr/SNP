#!/usr/bin/env python3

import sys
import os
import subprocess
import contextlib

#make directory to store output files
#subprocess.run("mkdir output")
#source_dir = './'
#target_dir = './output/'

#input files (fa1 and fa2) must be unzipped fasta files 
file = ""
fasta = ('.fa', '.fasta', '.fna')
try:
    fa1 = sys.argv[1]
    print("Reference file:", fa1)
    if not fa1.endswith(fasta):
        raise ValueError("IS EITHER ZIPPED OR NOT A FASTA FILE")
    fa2 = sys.argv[2]
    print("Query file:", fa2)
    if not fa2.endswith(fasta):
        raise ValueError("IS EITHER ZIPPED OR NOT A FASTA FILE")
except ValueError:
        print("FASTA FILES END WITH FA, FNA, OR FASTA. WHAT YOU GOT IS ZIPPED OR NOT A FASTA FILE YOU NOOB")

#align genome to genome with inputs from sys
def alignment(fa1, fa2): #wrapper for GSAlign
    rtn = subprocess.run(f"GSAlign -r {fa1} -q {fa2} -o output",  stdout=subprocess.PIPE, shell=True)
    log = rtn.stdout
    with open(f"{output}.vcf","r") as align_file:
        for line in align_file:
            line = line.rstrip()    
   # with open("log.txt", "w") as 
    alignment(fa1, fa2)





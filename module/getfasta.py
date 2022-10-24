#!/usr/bin/env python3



#pybedtools to get fasta seqns for translation of protein sequence
import pybedtools

with open('test.txt', 'r') as file:
    data = file.read().rstrip()
    a = pybedtools.BedTool(data, from_string=True)
    fasta = pybedtools.example_filename('test.fa')
    a = a.sequence(fi=fasta)
    w = open('test.fasta', 'w')
    w.write(open(a.seqfn).read())
    w.close()

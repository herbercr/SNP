#!/usr/bin/env python3

import sys, re
import pyranges as pr
gff_in=sys.argv[1]
Chrs=[]
databs=[]
features=[]
starts=[]
ends=[]
scores=[]
strands=[]
phases=[]
genes=[]
UniProts=[]
with open(gff_in,'r') as gff:
        for line in gff:
            if line.startswith('#'):
                continue
            if line.startswith('##'):
                continue
            line=line.rstrip()
            Chr, datab, feature, start, end, score, strand, phase, attributes=line.split('\t')
            gene=re.search(r"gene=(\w+\-\d+)", attributes)
            uniprotID=re.search(r'UniProtKB\/Swiss-Prot:(\w+)',attributes)
            Chrs.append(Chr)
            databs.append(datab)
            features.append(feature)
            starts.append(start)
            ends.append(end)
            scores.append(score)
            strands.append(strand)
            phases.append(phase)
            genes.append(gene.group(1))
            if not uniprotID:
                UniProts.append('NA')
            else:
                UniProts.append(uniprotID.group(1))
            
NewRange=pr.from_dict({'Chromosome':Chrs,'Start':starts,'End':ends,'Strand':strands,'Gene':genes,'Feature':features,'Prot':UniProts})
print(NewRange)

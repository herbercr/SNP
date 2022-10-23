#!/usr/bin/env python3
import pyranges as pr
chromosome_list = []
start = []
end = []
snp_data = []
ref_list = []
alt_list = []
snp_type = []
with open('reference_alignments.vcf', 'r') as vcf_file:
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
pyranges_df = pr.from_dict(test_dictionary)
insertion_subset = (pyranges_df.SNPtype == "TYPE=INSERT")
indel_subset = (pyranges_df.SNPtype == ("TYPE=DELETE" and "TYPE=INSERT"))
substitute_subset = (pyranges_df.SNPtype == "TYPE=SUBSTITUTE")

pandas_df = pyranges_df.as_df()
#print(pandas_df)

import sys, re
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
            if not gene:
                genes.append('NA')
            else:
                genes.append(gene.group(1))
            if not uniprotID:
                UniProts.append('NA')
            else:
                UniProts.append(uniprotID.group(1))

NewRange=pr.from_dict({'Chromosome':Chrs,'Start':starts,'End':ends,'Strand':strands,'Gene':genes,'Feature':features,'Prot':UniProts})
#print(NewRange)
cds_subset = (NewRange.Feature == 'CDS')
pyranges_coding = NewRange[cds_subset]
test_df= pyranges_coding.as_df()
#print(test_df.loc[:,['Start','End']])

i = 0
range_list = []
for num in range(int(test_df.shape[0])):
    range_value = range((int(test_df.iloc[num, 1])), int(test_df.iloc[num,2]))
    range_list.append(range_value)
    i = i+1
test_df["NTRanges"] = range_list
#for numbers in range(int(test_df.shape[0])):


























all_annotated_genes = []
all_annotated_features = []
all_annotated_proteins = []



for num in range(int(pandas_df.shape[0])):
    snp_position = pandas_df.iloc[num,1]
    annotated_genes = []
    annotated_features = []
    annotated_proteins = []
    for numbers in range(int(test_df.shape[0])):
        if snp_position in test_df.iloc[numbers, 7]:
            annotated_genes.append(test_df.iloc[numbers, 4])
            annotated_features.append(test_df.iloc[numbers, 5])
            annotated_proteins.append(test_df.iloc[numbers, 6])
            break 
    if len(annotated_genes) == 0:
        annotated_genes.append('NA')
        annotated_features.append('NA')
        annotated_proteins.append('NA')
    all_annotated_genes.extend(annotated_genes)
    all_annotated_features.extend(annotated_features)
    all_annotated_proteins.extend(annotated_proteins)
pandas_df["GeneAnnotation"] = all_annotated_genes
pandas_df['AnnotatedFeatures'] = all_annotated_features
pandas_df['AnnotataedProteins'] = all_annotated_proteins
print(len(all_annotated_genes))


print(pandas_df)



#isolate position from a row (need to be able to iterate through rows)
#search each row of gff dataframe (NTRanges column) for match
#if match present, pull gene, protein, feature to separate lists
#if not present, put NA in list
#iterate thru all rows in VCF dataframe
#when done append lists as a new column to table

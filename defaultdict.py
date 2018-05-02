#!/usr/bin/env python3
from Bio import SeqIO
# open GFF file
watermelon = open("watermelon.gff")

# read and store genome
genome = open("watermelon.fsa").read()

import sys
for line in watermelon:
# split string into list based on tabs
        positions = line.split("\t")
        start = int(positions[3])
        end = int(positions[4])
        gene = (positions[8])
        print(">" + gene + genome[start:end])
        

from collections import defaultdict
# declare the dictionary
gene_dict = defaultdict(dict)
# add an element
gene_dict[start] = gene
gene_dict[1] = 'cox1'
gene_dict[29747] = 'rpl2'
gene_dict[70073] = 'nad2'
# print it
print(gene_dict[1])
print(gene_dict[29747])
print(gene_dict[70073])

# add an element
gene_dict = (1:'cox1', 29747:'rpl2', 70073:'nad2') 

# print all of them
for num in gene_dict.keys():
	print(“gene”, num, “is”, gene_dict.get(num))


# print all of them
for num, name in gene_dict.items():
	print(“gene”, num, “is”, name)









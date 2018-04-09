#!/usr/bin/env python3
from Bio import SeqIO

# read and store genome
genome = open("watermelon.fsa").read()

# open GFF file

# read it in line by line

        # split string on tab into list
# use start and end coordinates to extract from genome


# open GFF file
watermelon = open("watermelon.gff")

import sys
for line in watermelon:
# split string into list based on tabs
        positions = line.split("\t")
        start = int(positions[3])
        end = int(positions[4])
        name = (positions[0])
        gene = (positions[8])
        print(">" + name + gene + genome[start:end])

# close GFF file

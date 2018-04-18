#!/usr/bin/env python3

from __future__ import print_function

# load the required modules
from Bio import SeqIO

from Bio.Seq import Seq

import argparse

import sys

# read and store genome
genome = open("watermelon_genes.fa").read()


# create an argument object ('parse') that will hold all the information necessary
parser = argparse.ArgumentParser(description="This script filters out sequences from a FASTA file that are shorter than a user a used specified length cutoff")

# use add_argument() method to add a positional argument

# positional arguments are *required* inputs, so their order/position matters

# argparse treats all options strings unless told to otherwise

parser.add_argument("fasta", help="name of FASTA file")

# add on optional argument, the length cutoff for our filter

parser.add_argument("-m","--min_seq_length", help= "filter sequences that are <= min_seq_length;default = 200 nt)", type=int,default=100)


# parse the arguments

args = parser.parse_args()


print("we're gonna open this FASTA file:", args.fasta)

print("filter sequences less than", args.min_seq_length, "nt in the length")

(species_name,type,begin,end)=line, split('\t')

# read and store genome
genome = open("watermelon.fsa").read()

# Usage
from Bio import SeqIO
import argparse

# create an argument object ('parse') that will hold all the information necessary
parser = argparse.ArgumentParser(description="Concatenate various sequences")
parser.add_argument('-f', action='store', dest='watermelon.fsa', help='Input fasta file')
result = parser.parse_args()
con_seq = ""

for rec in SeqIO.parse(result.fasta_file, "fasta"):
    con_seq += rec.seq

rc_con_seq = Seq(str(con_seq)).reverse_complement()
print rc_con_seq, len(rc_con_seq)

# open GFF file

# read it in line by line

        # split string on tab into list
# use start and end coordinates to extract from genome


# open GFF file
watermelon = open("watermelon.gff")


for line in watermelon:
# split string into list based on tabs
        positions = line.split("\t")
        start = int(positions[3])
        end = int(positions[4])
        name = (positions[0])
        gene = (positions[8])
        print(">" + name + gene + genome[start:end])



# close GFF file

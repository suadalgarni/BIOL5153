#! /usr/bin/env python3

# this script will parse a GFF file, extracting sequences for the annotated features

# load required modules
import sys
import os
import re
import argparse
from Bio import SeqIO


def get_args():
	# create an ArgumentParser object ('parser')
	parser = argparse.ArgumentParser()

	# add required/positional arguments
	parser.add_argument("gff",   help="name of GFF file")
	parser.add_argument("fasta", help="name of FASTA file")

	# parse the arguments
	return parser.parse_args()


def parse_fasta():
	# open and read the FASTA file
	genome = SeqIO.read(args.fasta, 'fasta')
	return genome.seq


def reverse_comp(dna):
	return dna.reverse_complement()


def parse_gff(dna):
	# open and parse the GFF file
	gff_file = open(args.gff, 'r')
	for line in gff_file:
		# split each line on a tab
		(seqid, source, feature, start, end, length, strand, phase, attributes) = line.split('\t')

		if(feature == 'CDS' or feature == 'tRNA' or feature == 'rRNA'):
			# split the attributes field
			atts = attributes.split(" ; ")
			# grab the gene name and, if present, the exon number
			gene = re.search("^Gene\s+(\S+)", atts[0])
			exon = re.search("exon\s+(\d+)",  atts[0])

			if(gene and exon):
				print(">" + seqid.replace(" ", "_") + "_" + gene.group(1) + "_" + exon.group(1))
			else:
				print(">" + seqid.replace(" ", "_") + "_" + gene.group(1))

			# extract the corresponding sequence
			fragment = dna[int(start)-1:int(end)]

			# print the sequence, either forward or reverse complemented
			if(strand == "+"):
				print(fragment)
			else:
				print(reverse_comp(fragment))
	gff_file.close()


def main():
	genome = parse_fasta()
	parse_gff(genome)

# get the command-line arguments
args = get_args()

main()
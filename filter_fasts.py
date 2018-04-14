#!/usr/bin/env python3

from Bio import SeqIO

# read and store genome
genome = open("watermelon_genes.fa").read()

# load the required modules

import argparse

# define our functions
def get_args():
    # create an argument object ('parse') that will hold all the information necessary

parser = argparse.ArgumentParser(description = "This script return the Fibonacci number at a specified position in the Fibonacci sequence")

    # define positional arguments
    parser.add_argument("num", help = "The Fibonacci number you wish to caculate", type = int)
    
    # define optional arguments
    parser.add_argument("-v", "--verbose", help = "Print verbose output", action = 'store_true')
    
    # parse the arguments
    parser.parse_args()

    # function to calculate the Fibonacci sequence
    def fib(n):

    
  # function do the calculation
   a,b = 0,1
   for i in range(args.num):
   a,b = b, a+b
   
   # return the value 
   return a  
   
def main():
   if args.verbose:
     print(fib(args.num))
      print("The Fibonacci number for", args.num, "is", fib(args.num))
    else:
        print(fib(args.num))
args = get_args()


   fib(args.num)

args = get_args()
   	   
main()
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


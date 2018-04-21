#!/usr/bin/env python3

from Bio import SeqIO


# declare our DNA seqeunce
dna=("ACTGATCGATTACGTATAGtatttGCTATCATACATATATATCGATGCGTTCAT")

# uppercase DNA sequence because it could contain a mix of upper- and lowercase characters
dna = dna.upper()

# print the upper-cased DNA sequence
print(dna)

############ start calculating nucleotide composition ############

# count each nucleotide in our DNA string
# NOTE: we're assuming that our sequence is just A,C,G, and T
a_count = dna.count('A')
g_count = dna.count('G')
c_count = dna.count('C')
t_count = dna.count('T')

# calculate the length of the DNA sequence
dna_length = len(dna)

# calculate GC fraction
gc = (g_count+c_count)/dna_length
# calculate AT fraction
at = (a_count+t_count)/dna_length

# print GC fraction to 2 decimal places
print( "%.2f" % gc)
#print( "%.2f" % at)

############ start calculating the reverse complement ############

# replace with complementary bases, making sure to substitute with lowercase so bases aren't overwritten/lost
compA1=(dna.replace("A", "t"))
compT1=(compA1.replace("T", "a"))
compC1=(compT1.replace("C", "g"))
compG1=(compC1.replace("G", "c"))

# we now have a mix of upper- and lowercase charcters in our DNA string, so uppercase everything again
dna_comp = compG1.upper()
#print(dna_comp)

# reverse the complemented DNA string
dna_comp = dna_comp[::-1]

# print the reverse complement
print(dna_comp)

# calculate GC content of the reverse complement
comp_g_count = dna_comp.count('G')
comp_c_count = dna_comp.count('C')


# print GC content of the reverse complement
print( "%.2f" % ((comp_g_count+comp_c_count)/dna_length))


############ trying it with BioPython now ############
print("Trying it with BioPython now")

for record in SeqIO.parse("sequences.fa", "fasta"):
    print(record.id)
    print ('sequence is ', record.seq)
    print ('reverse complement is ', record.seq.reverse_complement())
    print(record.format("phylip"))
#! /usr/bin/env python

# input: A protein string of length at most 1000 aa.
#output: The total number of different RNA strings from which the protein
#	could have been translated, modulo 1,000,000. (Don't neglect the 
#	importance of the stop codon in protein translation.)

import sys

with open(sys.argv[1]) as infile:
	aa_seq = infile.readline().strip()

protein = {
'A': ['GCU','GCC','GCA','GCG'],
'C': ['UGU','UGC'],
'D': ['GAU','GAC'],
'E': ['GAA','GAG'],
'F': ['UUC','UUU'],
'G': ['GGU','GGC','GGA','GGG'],
'H': ['CAU','CAC'],
'I': ['AUU','AUC','AUA'],
'K': ['AAA','AAG'],
'L': ['UUA','UUG','CUU','CUC','CUA','CUG'],
'M': ['AUG'],
'N': ['AAU','AAC'],
'P': ['CCU','CCC','CCA','CCG'],
'Q': ['CAA','CAG'],
'R': ['CGU','CGC','CGA','CGG','AGA','AGG'],
'S': ['UCC','UCA','UCG','AGU','AGC','UCU'],
'Stop': ['UAA','UGA','UAG'],
'T': ['ACU','ACC','ACA','ACG'],
'V': ['GUU','GUC','GUA','GUG'],
'W': ['UGG'],
'Y': ['UAC','UAU'],
}

mrna = 1
for aa in aa_seq:
	mrna *= len(protein[aa])
	
mrna*= len(protein['Stop'])

print mrna % 1000000

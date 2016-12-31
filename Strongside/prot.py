#! /usr/bin/env python

# Translating RNA to Protein http://rosalind.info/problems/prot/
# input: An RNA string s corresponding to a strand of mRNA (of length at
#	most 10 kbp).
#output: The protein string encoded by s.

import sys

with open(sys.argv[1]) as infile:
	rna = infile.readline().strip()

protein = {
'UUU': 'F' , 'UCU': 'S' , 'UAU': 'Y' , 'UGU': 'C', 'UUC': 'F', 'UCC': 'S',
'UAC': 'Y', 'UGC': 'C', 'UUA': 'L', 'UCA': 'S', 'UAA': 'Stop', 'UGA': 'Stop',
'UUG': 'L', 'UCG': 'S', 'UAG': 'Stop', 'UGG': 'W', 'CUU': 'L', 'CCU': 'P',
'CAU': 'H', 'CGU': 'R', 'CUC': 'L', 'CCC': 'P', 'CAC': 'H', 'CGC': 'R',
'CUA': 'L', 'CCA': 'P', 'CAA': 'Q', 'CGA': 'R', 'CUG': 'L', 'CCG': 'P',
'CAG': 'Q', 'CGG': 'R', 'AUU': 'I', 'ACU': 'T', 'AAU': 'N', 'AGU': 'S',
'AUC': 'I', 'ACC': 'T', 'AAC': 'N', 'AGC': 'S', 'AUA': 'I', 'ACA': 'T',
'AAA': 'K', 'AGA': 'R', 'AUG': 'M', 'ACG': 'T', 'AAG': 'K', 'AGG': 'R',
'GUU': 'V', 'GCU': 'A', 'GAU': 'D', 'GGU': 'G', 'GUC': 'V', 'GCC': 'A',
'GAC': 'D', 'GGC': 'G', 'GUA': 'V', 'GCA': 'A', 'GAA': 'E', 'GGA': 'G',
'GUG': 'V', 'GCG': 'A', 'GAG': 'E', 'GGG': 'G'}

prot = ''

for i in range(0, len(rna), 3):
	nuc = rna[i:i+3]
	if protein[nuc] != 'Stop':
		prot += protein[nuc]
	else:
		break
	
print prot

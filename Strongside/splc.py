#! /usr/bin/env python

# RNA Splicing http://rosalind.info/problems/splc/
# input: A DNA string s (of length at most 1 kbp) and a collection of 
#	substrings of s acting as introns. All strings are given in FASTA 
#	format.
#output: A protein string resulting from transcribing and translating 
#	the exons of s. (Note: Only one solution will exist for the dataset 
#	provided.)

import sys
import re

with open(sys.argv[1]) as infile:
	fna = [line.strip() for line in infile.readlines()]
	
dna = ''
introns = []
seq = ''
for line in fna:
	if line[0] == '>':
		if len(seq) > 0:
			if len(dna) == 0:
				dna = seq
			else:
				introns.append(seq)
			seq = ''
	else:
		seq += line
		
introns.append(seq)

for intron in introns:
	dna = dna.replace(intron, '')
	
rna = dna.replace('T', 'U')
	
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

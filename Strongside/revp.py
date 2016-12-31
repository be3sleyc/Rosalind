#! /usr/bin/env python

# Locating Restriction Sites http://rosalind.info/problems/revp/
# input: A DNA string of length at most 1 kbp in FASTA format.
#output: The position and length of every reverse palindrome in the 
#	string having length between 4 and 12. You may return these pairs in
#	any order.

def compliment(dna_seq):
	rc_dna = ''
	for n in dna_seq:
		if n == 'A':
			rc_dna += 'T'
		elif n == 'C':
			rc_dna += 'G'
		elif n == 'G':
			rc_dna += 'C'
		elif n == 'T':
			rc_dna += 'A'
	return rc_dna

import sys

with open(sys.argv[1]) as infile:
	dna = ''.join([line.strip() for line in infile.readlines()][1:])

rcdna = compliment(dna)

matches = []
for i in range(len(dna)):
	for j in range(4,13):
		if i+j <= len(dna):
			if dna[i:i+j] == str(rcdna[i:i+j])[::-1]:
				matches.append(str(i + 1) + ' ' + str(j))
			
print '\n'.join(matches)

#! /usr/bin/env python
# input: Two DNA strings s and t of equal length (not exceeding 1 kbp).
#output: The Hamming distance dH(s,t)

import sys

with open(sys.argv[1]) as infile:
	dna = [line.strip() for line in infile.readlines()]
	s = dna[0]
	t = dna[1]

ham = 0	
for i in range(len(s)):
	if s[i] != t[i]:
		ham += 1

print ham

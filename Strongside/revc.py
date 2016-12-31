#! /usr/bin/env python

# Complementing a Strand of DNA http://rosalind.info/problems/revc/
# input: A DNA string s of length at most 1000 bp.
#output: The reverse complement sc of s.

import sys

with open(sys.argv[1]) as infile:
	s = infile.readline().strip()
	
sc = ""

for n in s:
	if n == "A": sc += "T"
	elif n == "C": sc += "G"
	elif n == "G": sc += "C"
	elif n == "T": sc += "A"

print sc[::-1]

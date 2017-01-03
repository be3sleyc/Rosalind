#! /usr/bin/env python

#Given: A DNA string s of length at most 1000 bp.
#Return: Four integers (separated by spaces) representing the respective
#	number of times that the symbols 'A', 'C', 'G', and 'T' occur in s. 
#	Note: You must provide your answer in the format shown in the sample output below.

# Sample Dataset
#	AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC
# Sample Output
#	20 12 17 21

import sys
from Bio.Seq import Seq

def main():
	with open(sys.argv[1]) as infile:
		seq = Seq(infile.readline().strip())
	
	nuccount = []
	for n in ["A", "C", "G", "T"]:
		nuccount.append(seq.count(n))
	print ' '.join(map(str,nuccount))
	
if __name__ == '__main__':
	main()

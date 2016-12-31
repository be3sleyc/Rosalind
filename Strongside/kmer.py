#! /usr/bin/env python

# input: A DNA string s in FASTA format (having length at most 100 kbp).
#output: The 4-mer composition of s.

import sys
from itertools import product

def main():
	with open(sys.argv[1]) as infile:
		s = ''.join([line[0].strip() if line[0] == '>' else line.strip() for line in infile.readlines()]).split('>')[1]
	
	kmers = [''.join(x) for x in product(['A','C','G','T'], repeat=4)]
	composition = {}
	for kmer in kmers:
		composition[kmer] = 0
			
	for i in range(len(s) -3):
		kmer = s[i:i+4]
		composition[kmer] += 1
	composition = [[key,value] for key, value in composition.items()]
	composition.sort()
	composition = ' '.join(map(str,[value for key, value in composition]))
	print composition
if __name__ == '__main__':
	main()

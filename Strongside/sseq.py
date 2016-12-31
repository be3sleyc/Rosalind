#! /usr/bin/env python

# input: Two DNA strings s and t (each of length at most 1 kbp) in FASTA
#	format.
#output: One collection of indices of s in which the symbols of t appear 
#	as a subsequence of s. If multiple solutions exist, you may return 
#	any one.

import sys

def spliced_motif(dna, motif):
	indices = []
	for i in range(len(dna)):
		if dna[i] == motif[0]:
			index = [i]
			j = 1
			i += 1
			while j < len(motif) and i < len(dna):
				if dna[i] == motif[j]:
					index.append(i)
					j+= 1
				i += 1
			
			if len(index) == len(motif):
				indices.append(index)
	return [x+1 for x in indices[0]]

def main():
	with open(sys.argv[1]) as infile:
		fna = ''.join([line[0].strip() if line[0] == '>' else line.strip() for line in infile.readlines()]).split('>')
		seq = fna[1]
		sub = fna[2]
	print ' '.join([str(x) for x in spliced_motif(seq, sub)])
	
if __name__ == '__main__':
	main()

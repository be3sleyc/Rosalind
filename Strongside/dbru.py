#! /usr/bin/env python

# Constructing a De Bruijn Graph http://rosalind.info/problems/dbru/
# input: A collection of up to 1000 DNA strings of equal length 
#	(not exceeding 50 bp) corresponding to a set S of (k+1)-mers.
#output: The adjacency list corresponding to the de Bruijn graph 
#	corresponding to S union S^rc.

import sys

def reverse_complement(A):
	B = A[::-1]
	B = B.replace('A', 'B')
	B = B.replace('C', 'D')
	B = B.replace('G', 'C')
	B = B.replace('T', 'A')
	B = B.replace('B', 'T')
	B = B.replace('D', 'G')
	return B

def deBruin(nodes):
	k = len(nodes[0]) - 1
	
	edges = []
	for node in nodes:
		edges.append([node[:k],node[-k:]])
	return edges

def main():
	with open(sys.argv[1]) as infile:
		seq = set(map(str.strip, infile.readlines()))

	rc_seq = set([])
	for read in seq:
		rc_seq.add(reverse_complement(read))
	seq = [x for x in seq | rc_seq]
	seq.sort()
	print '('+')\n('.join([', '.join(x) for x in deBruin(seq)])+')'
	
	
if __name__ == '__main__':
	main()

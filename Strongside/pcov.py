#! /usr/bin/env python

# Genome Assembly with Perfect Coverage http://rosalind.info/problems/pcov/
# input: A collection of (error-free) DNA k-mers (k<=50) taken from the 
#	same strand of a circular chromosome. In this dataset, all k-mers 
#	from this strand of the chromosome are present, and their de Bruijn 
#	graph consists of exactly one simple cycle.
#output: A cyclic superstring of minimal length containing the reads 
#	(thus corresponding to a candidate cyclic chromosome).

import sys
import time

def graph(nodes):
	k = len(nodes[0]) -1
	path = nodes.pop(0)
	while len(nodes) > 0:
		for i in range(len(nodes)):
			if path.startswith(nodes[i][-k:]):
				node = nodes.pop(i)
				path = node[0]+path
				break
			if path.endswith(nodes[i][:k]):
				node = nodes.pop(i)
				path += node[-1]
				break
	return path[k:]

def main():
	with open(sys.argv[1]) as infile:
		reads = map(str.strip, infile.readlines())
		
	superstring = graph(reads)
	print superstring
	
if __name__ == '__main__':
	main()

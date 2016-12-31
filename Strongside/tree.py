#! /usr/bin/env python

# input: A positive integer n (n<=1000) and an adjacency list 
#	corresponding to a graph on n nodes that contains no cycles.
#output: The minimum number of edges that can be added to the graph to 
#	produce a tree.

import sys

def main():
	with open(sys.argv[1]) as infile:
		n = int(infile.readline().strip())
		adj_list = [line.strip().split() for line in infile.readlines()]
	
	print n-1-len(adj_list)
	
if __name__ == '__main__':
	main()

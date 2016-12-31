#! /usr/bin/env python

# Counting Subsets http://rosalind.info/problems/sset/
#Given: A positive integer n (n<=1000).
#Return: The total number of subsets of {1,2,...,n} modulo 1,000,000.

import sys
from itertools import product
def main():
	with open(sys.argv[1]) as infile:
		n = int(infile.readline().strip())
	
	print 2**n % 1000000
	
if __name__ == '__main__':
	main()

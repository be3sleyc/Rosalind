#! /usr/bin/env python

# input: A collection of at most 10 symbols defining an ordered alphabet
#	, and a positive integer n (n<=10).
#output: All strings of length n that can be formed from the alphabet, 
#	ordered lexicographically.

import sys
from itertools import product as perm

with open(sys.argv[1]) as infile:
	alphabet = infile.readline().strip().split()
	l = int(infile.readline().strip())
	
lex = perm(alphabet, repeat=l)

lex = [''.join(group) for group in lex]
print '\n'.join(sorted(lex))

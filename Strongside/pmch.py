#! /usr/bin/env python

# input:An RNA string s of length at most 80 bp having the same number 
#	of occurrences of 'A' as 'U' and the same number of occurrences of 
#	'C' as 'G'.
#output: The total possible number of perfect matchings of base pair 
#	edges in the bonding graph of s.

import sys
import math

with open(sys.argv[1]) as infile:
	s = ''.join([x.strip()[0] if x[0] == '>' else x.strip() for x in infile.readlines()]).split('>')[1]
	
acgu = [s.count('A'), s.count('C')]

perfect_matches = math.factorial(acgu[0]) * math.factorial(acgu[1])
print perfect_matches

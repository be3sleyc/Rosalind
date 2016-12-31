#! /usr/bin/env python

# Input: A DNA string s of length at most 1000 nt.
#Output: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

import sys

with open(sys.argv[1]) as infile:
	s = infile.readline().strip().lower()

a, c, g, t = 0, 0, 0, 0

for n in s:
	if n == 'a':
		a +=1
	elif n == 'c':
		c +=1
	elif n == 'g':
		g +=1
	elif n == 't':
		t +=1
		

print a, c, g, t

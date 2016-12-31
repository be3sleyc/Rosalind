#! /usr/bin/env python

# Finding a motif in DNA http://rosalind.info/problems/subs/
# input: Two DNA strings s and t(each of length at most 1 kbp).
#output: All locations of t as a substring of s.

import sys

with open(sys.argv[1]) as infile:
	s = infile.readline().strip()
	t = infile.readline().strip()
	
indices = []
n = len(t)

for i in range(len(s)):
	if s[i:i+n] == t:
		indices.append(i+1)
		
print ' '.join([str(x) for x in indices])

#! /usr/bin/env python

# Enumerating Gene Order http://rosalind.info/problems/perm/
# input: A positive integer n<=7.
#output: The total number of permutations of length n, followed by a 
#	list of all such permutations (in any order).

import sys
import itertools

with open(sys.argv[1]) as infile:
	n = int(infile.read().strip())
groups = []
size = 0
for group in itertools.permutations(range(1,n+1)):
	size += 1
	groups.append(' '.join([str(x) for x in group]))

print size
print '\n'.join(groups)

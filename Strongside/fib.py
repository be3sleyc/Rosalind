#! /usr/bin/env python

# input: Positive integers n <= 40 and k <= 5.
#output: The total number of rabbit pairs that will be present after n 
#	months, if we begin with 1 pair and in each generation, every pair 
#	of reproduction-age(at least 2 months old) rabbits produces a litter
#	of k rabbit pairs (instead of only 1 pair).

import sys

with open(sys.argv[1]) as infile:
	s = infile.readline().strip().split()

n = int(s[0]) - 2
k = int(s[1])

rp = [1,1] # rabbit pairs

while n > 0:
	rp.append(rp[-1] + rp[-2]*k)
	n -= 1

print rp[-1]

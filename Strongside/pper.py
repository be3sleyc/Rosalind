#! /usr/bin/env python

# Partial Permutations http://rosalind.info/problems/pper/
# input: Positive integers n and k such that 100>=n>0 and 10>=k>0.
#output: The total number of partial permutations P(n,k), modulo 1,000,000.

import sys
import math

with open(sys.argv[1]) as infile:
	n, k = [int(x) for x in infile.readline().strip().split()]

print ((math.factorial(n))/math.factorial(n-k)) % 1000000

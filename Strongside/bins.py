#! /usr/bin/env python

# Input: Two positive integers n<=10^5 and m<=10^5, a sorted array A[1..n]
#	of integers from -10^5 to 10^5 and a list of m integers 
#	-10^5<=k_1,k_2,...,k_m<=10^5.
#Output: For each k_i, output an index 1<=j<=n s.t. A[j]=k_i or "-1" if 
#	there is no such index.

import sys
import time

def binarysearch(term, search_space, n):
	bottom = 0
	top = n
	
	while bottom + 1 != top:
		test = (top + bottom)/2
		if search_space[test] > term:
			top = test
		else:
			bottom = test
	if search_space[bottom] == term:
		return bottom +1
	else:
		return -1

with open(sys.argv[1]) as infile:
	n = int(infile.readline().strip())
	m = int(infile.readline().strip())
	A = [int(x) for x in infile.readline().strip().split()]
	I = [int(x) for x in infile.readline().strip().split()]

solution = []
for num in I:
	solution.append(binarysearch(num, A, n))
	
print ' '.join([str(x) for x in solution])


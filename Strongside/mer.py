#! /usr/bin/env python

# input: A positive integer n<=10^5 and a sorted array A[1..n] of 
#	integers from -10^5 to 10^5, a positive integer m<=10^5 and a sorted
#	array B[1..m] of integers from -10^5 to 10^5.
#output: A sorted array C[1..n+m] containing all the elements of A and B.

import sys
import time

def merge(left, right):
	time.sleep(0)
	result = []
	
	while len(left) > 0 and len(right) > 0:
		if left[0] <= right[0]:
			result.append(left.pop(0))
		else:
			result.append(right.pop(0))
	result += left
	result += right
	return result

with open(sys.argv[1]) as infile:
	n = int(infile.readline().strip())
	A = [int(x) for x in infile.readline().strip().split()]
	m = int(infile.readline().strip())
	B = [int(x) for x in infile.readline().strip().split()]

print ' '.join([str(x) for x in merge(A, B)])

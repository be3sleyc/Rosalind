#! /usr/bin/env python

# Merge Sort http://rosalind.info/problems/ms/
# input: A positive integer n<=10^5 and an array A[1..n] of integers from 
#	-105 to 105.
#output: A sorted array A[1..n].

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
	
def mergesort(Alist):
	if len(Alist) <= 1:
		return Alist
	
	left = []
	right = []
	m = len(Alist)/2
	for i in range(len(Alist)):
		if i < m:
			left.append(Alist[i])
		else:
			right.append(Alist[i])
		
	left = mergesort(left)
	right = mergesort(right)
	return merge(left, right)
	

with open(sys.argv[1]) as infile:
	n = int(infile.readline().strip())
	A = [int(x) for x in infile.readline().strip().split()]

A= mergesort(A)

print ' '.join([str(x) for x in A])

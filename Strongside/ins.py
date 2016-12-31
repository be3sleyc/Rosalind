#! /usr/bin/env python

# Insertion Sort http://rosalind.info/problems/ins/
#Given: A positive integer n<=10^3 and an array A[1..n] of integers.
#Return: The number of swaps performed by insertion sort algorithm on 
#	A[1..n].

import sys

def Ins_sort(A):
	global swaps

	for i in range(1,len(A)):
		k = i
		while k > 0 and A[k] < A[k-1]:
			temp = A[k]
			A[k] = A[k-1]
			A[k-1] = temp
			swaps += 1
			k -= 1

		

with open(sys.argv[1]) as infile:
	n = int(infile.readline().strip())
	A = [int(x) for x in infile.readline().strip().split()]
	
swaps = 0
Ins_sort(A)

print swaps


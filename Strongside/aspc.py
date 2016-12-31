#! /usr/bin/env python

# Introduction to Alternative Splicing http://rosalind.info/problems/aspc/
#Given: Positive integers n and m with 0<=m<=n<=2000.
#Return: The sum of combinations C(n,k) for all k satisfying m<=k<=n, modulo 1,000,000.

import sys
from math import factorial

def nCr(n, r):
	if n < 0 or r < 0:
		print n, r
		return -1
	else:
		return factorial(n)/(factorial(r)*factorial(n - r))

def main():
	with open(sys.argv[1]) as infile:
		n,m = map(int, infile.readline().strip().split())
	combo_sum = 0
	k = m
	while k <= n:
		combo_sum += nCr(n, k)
		k += 1
		
		
	print combo_sum % 1000000
	
if __name__ == '__main__':
	main()

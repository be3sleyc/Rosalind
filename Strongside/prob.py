#! /usr/bin/env python

# input: A DNA string s of length at most 100 bp and an array A 
#	containing at most 20 numbers between 0 and 1.
#output: An array B having the same length as A in which B[k] represents
#	the common logarithm of the probability that a random string 
#	constructed with the GC-content found in A[k] will match s exactly.

import sys
import math

def main():
	with open(sys.argv[1]) as infile:
		s = infile.readline().strip()
		a = [float(x) for x in infile.readline().strip().split()]

	b = [0] * len(a)
	
	for i in range(len(a)):
		for j in range(len(s)):
			if s[j] in 'GC':
				b[i] += math.log10(0.5*a[i])  
			else:
				b[i] += math.log10(0.5*(1-a[i]))
		
	print ' '.join(['%.3f'  % x for x in b])
	 

if __name__ == '__main__':
	main()

#! /usr/bin/env python

# Enumerating Oriented Gene Orderings http://rosalind.info/problems/sign/
# input: A positive integer n<=6.
#output: The total number of signed permutations of length n, followed 
#	by a list of all such permutations (you may list the signed 
#	permutations in any order).

import sys
from itertools import product
from itertools import permutations

def matmul(x, y):
	return [a*b for a,b in zip(x,y)]

def main():
	with open(sys.argv[1]) as infile:
		n = int(infile.readline().strip())
	
	num = []
	for i in range(1,n+1):
		num.append(i)
	
	signed = [x for x in product([-1, 1], repeat=n)]
	
	perms = [x for x in permutations(num, n)]
	
	signed_perms = []
	for p in perms:
		for s in signed:
			signed_perms.append(matmul(p,s))
	
	
	print len(signed_perms)
	print '\n'.join([' '.join([str(t) for t in x]) for x in signed_perms])
	
	
	
if __name__ == '__main__':
	main()

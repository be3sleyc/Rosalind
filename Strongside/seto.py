#! /usr/bin/env python

# Introduction to Set Operations http://rosalind.info/problems/seto/
#Given: A positive integer n (n<=20,000) and two subsets A and B of {1,2,...,n}.
#Return: Six sets: A union B, A intersect B, A-B, B-A, A^c, and B^c 
#	(where set complements are taken with respect to {1,2,...,n}).

import sys

def main():
	with open(sys.argv[1]) as infile:
		n = int(infile.readline().strip())
		A = set([int(x) for x in ''.join(infile.readline().strip()[1:-1]).split(', ')])
		B = set([int(x) for x in ''.join(infile.readline().strip()[1:-1]).split(', ')])
		
	N = set([x for x in range(1,n+1)])

	print '{'+', '.join(map(str, A | B))+'}'
	print '{'+', '.join(map(str, A & B))+'}'
	print '{'+', '.join(map(str, A - B))+'}'
	print '{'+', '.join(map(str, B - A))+'}'
	print '{'+', '.join(map(str, N - A))+'}'
	print '{'+', '.join(map(str, N - B))+'}'
	
	
if __name__ == '__main__':
	main()

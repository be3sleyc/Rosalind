#! /usr/bin/env python

# Creatring a distance matrix http://rosalind.info/problems/pdst/
# Given: A collection of n (n≤10) DNA strings s1,...,sn of equal length 
#	(at most 1 kbp). Strings are given in FASTA format.
# Return: The matrix D corresponding to the p-distance dp on the given 
#	strings. As always, note that your answer is allowed an absolute 
#	error of 0.001. 

import sys

def p_distance(A, B):
	ln = len(A)
	dif = 0.0
	for i in range(ln):
		if A[i] != B[i]:
			dif += 1.0
	return dif/ln
		

def main():
	with open(sys.argv[1]) as infile:
		fna = ''.join([line[0].strip() if line[0] == '>' else line.strip() for line in infile.readlines()]).split('>')[1:]
	
	pdist = []
	for i in range(len(fna)):
		row = []
		for j in range(len(fna)):
			pd = p_distance(fna[i], fna[j])
			row.append(pd)
		pdist.append(row)
				
	print '\n'.join([' '.join(['%.5f' % x for x in row]) for row in pdist])
	
if __name__ == '__main__':
	main()

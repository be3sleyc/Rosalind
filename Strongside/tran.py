#! /usr/bin/env python

# Transitions and Transversions http://rosalind.info/problems/tran/
# input: Two DNA strings s1 and s2 of equal length (at most 1 kbp).
#output: The transition/transversion ratio R(s_1,s_2).

import sys

# A<->G
# T<->C
def transition(a, b):
	ition = 0
	for i in range(len(a)):
		if a[i] == 'A':
			if b[i] == 'G':
				ition += 1
		elif a[i] =='G':
			if b[i] == 'A':
				ition += 1
		elif a[i] =='T':
			if b[i] == 'C':
				ition += 1
		elif a[i] =='C':
			if b[i] == 'T':
				ition += 1
	return float(ition)
	
# A,G <-> T,C
def transversion(a, b):
	version = 0
	for i in range(len(a)):
		if a[i] in 'AG':
			if b[i] in 'CT':
				version += 1
		elif a[i] in 'CT':
			if b[i] in 'AG':
				version += 1
	return float(version)

def main():
	with open(sys.argv[1]) as infile:
		fna = ''.join([line[0].strip() if line[0] == '>' else line.strip() for line in infile.readlines()]).split('>')
		s1 = fna[1]
		s2 = fna[2]
		
	print transition(s1, s2)/ transversion(s1, s2)
		

if __name__ == '__main__':
	main()

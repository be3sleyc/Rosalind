#! /usr/bin/env python

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

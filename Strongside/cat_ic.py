#! /usr/bin/env python

# input: An RNA string s having the same number of occurrences of 'A' as
#	'U' and the same number of occurrences of 'C' as 'G'. The length of 
#	the string is at most 300 bp.
#output: The total number of noncrossing perfect matchings of basepair
#	edges in the bonding graph of s, modulo 1,000,000.

import sys

#c_n = sum(n, k=1: c_k-1*c_n-k)
def catalan(s):
	c = [1,1]
	AG = [s.count('A'),s.count('G')]
	k = 1
	while k <= AG[0]:
		cn = c[k-1] + (c[k - 1] * c[AG[0]-k])
		c.append(cn)
		k += 1
	return c[-1]
	

def main():
	with open(sys.argv[1]) as infile:
		s = ''.join([line[0].strip() if line[0] == '>' else line.strip() for line in infile.readlines()]).split('>')[1]
	print catalan(s)
	
	
if __name__ == '__main__':
	main()

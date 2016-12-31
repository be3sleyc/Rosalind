#! /usr/bin/env python

# Speeding up Motif Finding http://rosalind.info/problems/kmp/
# input: A DNA string s (of length at most 100 kbp) in FASTA format.
#output: The failure array of s.

import sys

def main():
	with open(sys.argv[1]) as infile:
		s = ''.join([line.strip() for line in infile.readlines()][1:])
		
	fail_arr = [0] * len(s)
	pos = 1
	cnd = 0
	while pos < len(s):	
		if s[pos] == s[cnd]:
			fail_arr[pos] = cnd +1 
			cnd += 1
			pos += 1
		elif cnd > 0:
			cnd = fail_arr[cnd-1]
		else:
			fail_arr[pos] = 0
			pos += 1
	
	
	print ' '.join(map(str,fail_arr))
	
if __name__ == '__main__':
	main()

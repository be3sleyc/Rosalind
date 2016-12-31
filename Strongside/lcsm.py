#! /usr/bin/env python

# Finding a Shared Motif http://rosalind.info/problems/lcsm/
# input: A collection of k (k<=100) DNA strings of length at most 1 kbp
#	each in FASTA format.
#output: A longest common substring of the collection. (If multiple
#	solutions exist, you may return any single solution.)

import sys

with open(sys.argv[1]) as infile:
	fna = [line.strip() for line in infile.readlines()]

dna = []
seq = ''

for line in fna:
	if line[0] == '>':
		if len(seq) > 1:
			dna.append(seq)
			seq = ''
	else:
		seq += line

dna.append(seq)

seq1 = ' '+dna.pop(0)
seq2 = ' '+dna.pop(0)

s = [[0 for x in range(len(seq2))] for y in range(len(seq1))]
longest = [0,0]
l_v = s[0][0]

for i in range(1,len(seq2)):
	for j in range(1,len(seq1)):
		if seq1[j] == seq2[i]:
			s[i][j] = 1+s[i-1][j-1]
			if s[i][j] > l_v:
				l_v = s[i][j]
				longest = [i,j]
			elif s[i][j] == l_v:
				longest.append(i)
				longest.append(j)
'''
print ' ',' '.join(seq1)
for i in range(len(s)):
	print seq2[i],' '.join(str(x) for x in s[i])
'''	
	
lcss = []
while len(longest) != 0:
	i = longest.pop(0)
	j = longest.pop(0)
	lcs = seq2[i]
	while len(lcs) < l_v:
		i -=1
		j -=1
		lcs = seq2[i] + lcs
	lcss.append(lcs)
	
for ss in lcss:
	for seq in dna:
		if ss not in seq:
			lcss.remove(ss)
		
print lcss[0]



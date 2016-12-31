#! /usr/bin/env python

# Computing GC Content http://rosalind.info/problems/gc/
# input: At most 10 DNA strings in FASTA format (of length at most 
#	1 kbp each).
#output: The ID of the string having the highest GC-content, followed by
#	the GC-content of that string. Rosalind allows for a default error 
#	of 0.001 in all decimal answers unless otherwise stated.

import sys

def gc(seq):
	g = seq.count('G')
	c = seq.count('C')
	#print float((g+c))/len(seq) * 100
	return float((g+c))/len(seq) * 100

with open(sys.argv[1]) as infile:
	fastas = [line.strip() for line in infile.readlines()]

ids = []
seqs = []
seq = ''
for line in fastas:
	if line[0] == '>':
		if(seq != ''):
			seqs.append(seq)
			seq = ''
		ids.append(line[1:])
	else:
		seq += line.upper()
if(seq != ''):
	seqs.append(seq)
	seq = ''

max_seq = 0
max_gc = gc(seqs[0])

for i in range(1,len(seqs)):
	if max_gc < gc(seqs[i]):
		max_seq = i
		max_gc = gc(seqs[i])
		
print ids[max_seq]
print str.format("{0:f}", max_gc)
	


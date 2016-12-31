#! /usr/bin/env python

# input:A collection of at most 10 DNA strings of equal length (at most 
#	1 kbp) in FASTA format.
#output: A consensus string and profile matrix for the collection. (If 
#	several possible consensus strings exist, then you may return any 
#	one of them.)

import sys

with open(sys.argv[1]) as infile:
	fna = infile.readlines()

seq = ''
dna = []
for line in fna:
	line = line.strip()
	if line[0] == '>':
		if len(seq) > 0:
			dna.append(seq)
		seq = ''
	else:
		seq += line
		
dna.append(seq)

A = [0]*len(seq)
C = [0]*len(seq)
G = [0]*len(seq)
T = [0]*len(seq)
consensus = ['']*len(seq)

for seq in dna:
	for i in range(len(seq)):
		if seq[i] == 'A':
			A[i] += 1
		elif seq[i] == 'C':
			C[i] += 1
		elif seq[i] == 'G':
			G[i] += 1
		elif seq[i] == 'T':
			T[i] += 1
			
for i in range(len(seq)):
	mx = max(A[i], C[i], G[i], T[i])
	if mx == A[i]:
		consensus[i] = 'A'
	elif mx == C[i]:
		consensus[i] = 'C'
	elif mx == G[i]:
		consensus[i] = 'G'
	elif mx == T[i]:
		consensus[i] = 'T'

print ''.join(consensus)
print 'A: ' + ' '.join([str(x) for x in A])
print 'C: ' + ' '.join([str(x) for x in C])
print 'G: ' + ' '.join([str(x) for x in G])
print 'T: ' + ' '.join([str(x) for x in T])


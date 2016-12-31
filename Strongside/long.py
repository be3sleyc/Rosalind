#! /usr/bin/env python

# Genome Assembly as shortest superstring http://rosalind.info/problems/long/
# input: At most 50 DNA strings whose length does not exceed 1 kbp in 
#	FASTA format (which represent reads deriving from the same strand of
#	a single linear chromosome).
#The dataset is guaranteed to satisfy the following condition: there 
#	exists a unique way to reconstruct the entire chromosome from these 
#	reads by gluing together pairs of reads that overlap by more than 
#	half their length.
#output: A shortest superstring containing all the given strings (thus 
#	corresponding to a reconstructed chromosome).

import sys
import time

def pair(seq, dna):
	global read_ln
	for i in range(len(dna)):
		for j in range(read_ln, read_ln/2, -1):
			if dna[i].endswith(seq[:j]):
				seq = dna.pop(i) + seq[j:]
				return seq, dna
				
			if seq.endswith(dna[i][:j]):
				seq += dna.pop(i)[j:]
				return seq, dna


with open(sys.argv[1]) as infile:
	reads = [line.strip() for line in infile.readlines()]

# separate dna sequences from fasta id tags
for i in range(len(reads)):
	if reads[i][0] == '>':
		reads[i] = reads[i][0]

reads = ''.join(reads[1:])
reads = reads.split('>')

# pair the reads
contig = reads.pop(0)
read_ln = len(reads[0])

while len(reads) > 0:
	contig, reads = pair(contig, reads)
	
	time.sleep(0)
		
print contig

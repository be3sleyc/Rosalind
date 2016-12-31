#! /usr/bin/env python

# Input: A collection of DNA strings in FASTA format having total length
#	at most 10 kbp.
#Output: The adjacency list corresponding to O_3. You may return edges 
#	in any order.

import sys
from Bio import SeqIO

with open(sys.argv[1]) as infile:
	fna = SeqIO.to_dict(SeqIO.parse(infile, "fasta"))
	
ids = [record for record in fna]

pairs = {}
for rec in ids:
	for rec2 in ids:
		if fna[rec].seq[:3] == fna[rec2].seq[-3:] and rec != rec2:
			if rec2 in pairs:
				pairs[rec2].append(rec)
			else:
				pairs[rec2] = [rec]

for k,v in pairs.items():
	for i in v:
		print k, i


#! /usr/bin/env python

# Finding a protein motif http://rosalind.info/problems/mprt/
# input: At most 15 UniProt Protein Database access IDs.
#output: For each protein possessing the N-glycosylation motif(N^P[ST]^P), output 
#	its given access ID followed by a list of locations in the protein 
#	string where the motif can be found.

import sys
import urllib
import re

with open(sys.argv[1]) as infile:
	proteins = [line.strip() for line in infile.readlines()]

pattern = re.compile('N[^P][ST][^P]')
pr_db = []
for prot in proteins:
	pr_db.append(''.join(urllib.urlopen("http://www.uniprot.org/uniprot/" + prot + ".fasta").read().split('\n')[1:-1]))

matches = []
for i in range(len(proteins)):
	matched = [proteins[i]]
	for m in range(len(pr_db[i])):
		if pattern.match(pr_db[i],m,m+4) != None:
			matched.append(m+1)
	if len(matched) > 1:
		matches.append(matched)

for m in matches:
	print m[0]
	print ' '.join([str(x) for x in m[1:]])


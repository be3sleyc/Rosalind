#! /usr/bin/env python

#Given: A collection of n (n<=10) GenBank entry IDs.
#Return: The shortest of the strings associated with the IDs in FASTA format.

import sys
from Bio import Entrez
from Bio import SeqIO

def main():
	with open(sys.argv[1]) as infile:
		entries = infile.readline().strip().split()
	
	Entrez.email = "beesleycrm@gmail.com"
	handle = Entrez.efetch(db='nucleotide', id=entries, rettype='fasta')
	records = list(SeqIO.parse(handle, 'fasta'))
	
	short = records.pop(0)
	for rec in records:
		if len(rec.seq) < len(short.seq):
			short = rec
	print short.format("fasta")
	
if __name__ == '__main__':
	main()

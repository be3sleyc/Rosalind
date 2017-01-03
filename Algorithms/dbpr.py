#! /usr/bin/env python

#Given: The UniProt ID of a protein.
#Return: A list of biological processes in which the protein is involved
#	(biological processes are found in a subsection of the protein's 
#	"Gene Ontology" (GO) section).

import sys
from Bio import ExPASy
from Bio import SwissProt

def main():
	with open(sys.argv[1]) as infile:
		handle = ExPASy.get_sprot_raw(infile.readline().strip())

	record = SwissProt.read(handle)
	print '\n'.join([ref[2][2:] if ref[0] == 'GO' and ref[2][0] == 'P' else '' for ref in record.cross_references]).strip()
	

if __name__ == '__main__':
	main()

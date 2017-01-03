#! /usr/bin/env python

#Pairwise Global Alignment
# Given: Two GenBank IDs.
#Return: The maximum global alignment score between the DNA strings 
#	associated with these IDs. 

import sys
import subprocess
from Bio import Entrez
from Bio import SeqIO

def main():
	with open(sys.argv[1]) as infile:
		genIDs = infile.readline().strip().split()
	
	Entrez.email = "beesleycrm@gmail.com"
	handle = Entrez.efetch(db='nucleotide', id=genIDs, rettype='fasta')
	records = list(SeqIO.parse(handle, 'fasta'))
	
	seqA = open('SeqA.fa', 'w')
	seqA.write(records[0].format("fasta"))
	seqB = open('SeqB.fa', 'w')
	seqB.write(records[1].format("fasta"))
	seqA.close()
	seqB.close()
	
	subprocess.call(["needle", "-asequence", "SeqA.fa", "-bsequence", "SeqB.fa", 
	"-gapopen", "10", "-gapextend", "1", "-endweight", "Y", "-endopen", "10", "-endextend", "1", 
	"-aformat3", "score", "-outfile", "score.txt"], shell = False)
	
	with open("score.txt") as scorefile:
		with open("../output.txt", 'w') as outfile:
			score = scorefile.readline().strip().split()[-1][1:-1]
			outfile.write(score)

if __name__ == '__main__':
	main()

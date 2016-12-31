#! /usr/bin/env python

# Open Reading Frames http://rosalind.info/problems/orf/
# input: A DNA string s of length at most 1 kbp in FASTA format.
#output: Every distinct candidate protein string that can be translated 
#	from ORFs of s. Strings can be returned in any order.
	
def ReadingFrames(dna_seq):
	rf = []
	for s in range(3):
		seq = dna_seq[s:]
		if len(seq) % 3 == 0:
			rf.append(seq)
		else:
			rf.append(seq[:len(seq) - len(seq) % 3])
	return rf

def Reverse_Complement(dna_seq):
	rc_dna = ''
	for n in dna_seq[::-1]:
		if n == 'A':
			rc_dna += 'T'
		elif n == 'C':
			rc_dna += 'G'
		elif n == 'G':
			rc_dna += 'C'
		elif n == 'T':
			rc_dna += 'A'
	return rc_dna
		
	
import sys

with open(sys.argv[1]) as infile:
	dna = ''.join([line.strip() for line in infile.readlines()][1:])

frames = ReadingFrames(dna)
frames += ReadingFrames(Reverse_Complement(dna))

dna_codons = {
'TTT': 'F', 'CTT': 'L', 'ATT': 'I', 'GTT': 'V',
'TTC': 'F', 'CTC': 'L', 'ATC': 'I', 'GTC': 'V',
'TTA': 'L', 'CTA': 'L', 'ATA': 'I', 'GTA': 'V',
'TTG': 'L', 'CTG': 'L', 'ATG': 'M', 'GTG': 'V',
'TCT': 'S', 'CCT': 'P', 'ACT': 'T', 'GCT': 'A',
'TCC': 'S', 'CCC': 'P', 'ACC': 'T', 'GCC': 'A',
'TCA': 'S', 'CCA': 'P', 'ACA': 'T', 'GCA': 'A',
'TCG': 'S', 'CCG': 'P', 'ACG': 'T', 'GCG': 'A',
'TAT': 'Y', 'CAT': 'H', 'AAT': 'N', 'GAT': 'D',
'TAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D',
'TAA': 'Stop', 'CAA': 'Q', 'AAA': 'K', 'GAA': 'E',
'TAG': 'Stop', 'CAG': 'Q', 'AAG': 'K', 'GAG': 'E',
'TGT': 'C', 'CGT': 'R', 'AGT': 'S', 'GGT': 'G',
'TGC': 'C', 'CGC': 'R', 'AGC': 'S', 'GGC': 'G',
'TGA': 'Stop', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G',
'TGG': 'W', 'CGG': 'R', 'AGG': 'R', 'GGG': 'G' 
}

proteins = set()
for frame in frames:
	for i in range(0,len(frame),3):
		codon = frame[i:i+3]
		aa = dna_codons[codon]
		if aa == 'M':
			prot = ''
			for c in range(i,len(frame),3):
				codon = frame[c:c+3]
				aa = dna_codons[codon]
				if aa == 'Stop':
					if len(prot) > 0 and prot[0] == 'M':
						proteins.add(prot)
					prot = ''
				else:
					prot += aa

print '\n'.join(proteins)

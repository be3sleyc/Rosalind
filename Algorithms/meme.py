#! /usr/bin/env python

#Given: A set of protein strings in FASTA format that share some motif 
#	with minimum length 20.
#Return: Regular expression for the best-scoring motif.

import sys
import subprocess
import xml.etree.ElementTree

def main():

	subprocess.call(["meme", sys.argv[1], "-protein", "-nmotifs", "1", "-nostatus" ], shell=False)
	
	output = xml.etree.ElementTree.parse("./meme_out/meme.xml").getroot()
	regex = output.find("motifs").find("motif").find("regular_expression").text.strip()
	
	print regex
	
if  __name__ == '__main__':
	main()

#! /usr/bin/env python

#Given: A genus name, followed by two dates in YYYY/M/D format.
#Return: The number of Nucleotide GenBank entries for the given genus 
#	that were published between the dates specified.

import sys
from Bio import Entrez

def main():
	with open(sys.argv[1]) as infile:
		name = infile.readline().strip()
		start_date = infile.readline().strip()
		end_date = infile.readline().strip()
	
	Entrez.email = "beesleycrm@gmail.com"
	handle = Entrez.esearch(db='nucleotide', term=name, datetype="pdat", mindate=start_date, maxdate=end_date)
	record = Entrez.read(handle)
	print record["Count"]
	
if __name__ == '__main__':
	main()

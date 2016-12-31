#! /usr/bin/env python

# Transcribing DNA to RNA http://rosalind.info/problems/RNA/
# input: A DNA string t having length at most 1000 nt.
#output: The transcribed RNA string of t.

import sys

with open(sys.argv[1]) as infile:
	t = infile.readline().strip()

u = t.replace("T", "U")

print u

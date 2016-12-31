#! /usr/bin/env python

# Mortal Fibonacci Rabbits http://rosalind.info/problems/fibd/
# input: Positive integers n <= 100 and m <= 20.
#output: The total number of pairs of rabbits that will remain after n
#	months, if all rabbits live for m months.

import sys

with open(sys.argv[1]) as infile:
	s = infile.readline().strip().split()

n = int(s[0]) # months
m = int(s[1]) # life
t = 1 # time

rp = [0] * m # array of rabbits at every year of life
rp[0] = 1	 # so far, only one rabbit at age 0

for month in range(n - 1): 		# cycle through the time given
	new_rabbits = sum(rp[1:]) 		# new rabbits will be equal to total reproducing rabbits
	rp = [new_rabbits] + rp[:m-1]	# cycle the rabbits through with the new rabbits at the beginning and the oldest rabbits deleted

print sum(rp) # return the sum of all rabbits at the end of time given

# solution provided by Sefa Kilic with code found at https://github.com/sefakilic/rosalind/blob/master/problems/fibd/fibd.py
# notes of understanding added

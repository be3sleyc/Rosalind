#! /usr/bin/env python

# input: Six positive integers, each of which does not exceed 20,000. 
#	The integers correspond to the number of couples in a population 
#	possessing each genotype pairing for a given factor. In order, the 
#	six given integers represent the number of couples having the 
#	following genotypes:
#    (0)AA-AA - 100%AA
#    (1)AA-Aa - 50% AA, 50% Aa
#    (2)AA-aa - 100% Aa
#    (3)Aa-Aa - 25% AA, 50% Aa, 25% aa
#    (4)Aa-aa - 50% Aa, 50% aa
#    (5)aa-aa - 100% aa

#output: The expected number of offspring displaying the dominant 
#	phenotype in the next generation, under the assumption that every 
#	couple has exactly two offspring.

import sys

with open(sys.argv[1]) as infile:
	parents = [int(x) for x in infile.readline().split()]
	
dom = 2*parents[0]
dom += 2*parents[1]
dom += 2*parents[2]
dom += 2*.75*parents[3]
dom += 2*.5*parents[4]
dom += 2*0*parents[5]

print dom

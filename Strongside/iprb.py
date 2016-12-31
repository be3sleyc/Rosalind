#! /usr/bin/env python

# Mendel's First Law http://rosalind.info/problems/iprb/
# input: Three positive integers k, m, and n, representing a population 
#	containing k+m+n organisms: k individuals are homozygous dominant 
#	for a factor, m are heterozygous, and n are homozygous recessive.
#output: The probability that two randomly selected mating organisms 
#	will produce an individual possessing a dominant allele (and thus 
#	displaying the dominant phenotype). Assume that any two organisms 
#	can mate.

import sys

with open(sys.argv[1]) as infile:
	pop = infile.readline().split()
k = float(pop[0]) #Homozygous Dominant
m = float(pop[1]) #Heterozygous
n = float(pop[2]) #Homozygous Recessive
total_pop = k+m+n

# HomoDom^2 = 4 HomoDom: ratio 1
prob_dom = k/total_pop * (k - 1)/(total_pop - 1) 
# HomoDom * Hetero = 2 HomoDom, 2 Hetero: ratio 1
prob_dom += k/total_pop * m/(total_pop - 1)
# HomoDom * HomoRec = 4 Hetero: ratio 1
prob_dom += k/total_pop * n/(total_pop - 1)
# Hetero * HomoDom = 2 HomoDom, 2 Hetero: ratio 1 
prob_dom += m/total_pop * k/(total_pop - 1) 
# Hetero^2 = 1/4 HomoDom, 1/2 Hetero, 1/4 HomoRec: ratio 0.75
prob_dom += 0.75 * (m/total_pop * (m - 1)/(total_pop - 1))
# Hetero * HomoRec = 1/2 Hetero, 1/2 HomoRec: ratio 0.5
prob_dom += 0.5 * (m/total_pop * (n)/(total_pop - 1))
# HomoRec * HomoDom = 4 Hetero: ratio 1
prob_dom += n/total_pop * k/(total_pop - 1)
# HomoRec * Hetero = 1/2 Hetero, 1/2 HomoRec: ratio 0.5
prob_dom += 0.5 * (n/total_pop * m/(total_pop - 1))
# HomoRec^2 = 4 HomoRec: ratio 0

print "%.5f" % prob_dom


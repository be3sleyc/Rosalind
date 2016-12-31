#! /usr/bin/env python

# Independant Alleles http://rosalind.info/problems/lia/
# input: Two positive integers k (k<=7) and N (N<=2k). In this problem, we 
#	begin with Tom, who in the 0th generation has genotype Aa Bb. Tom has 
#	two children in the 1st generation, each of whom has two children, and 
#	so on. Each organism always mates with an organism having genotype Aa Bb
#	.
#output: The probability that at least N Aa Bb organisms will belong to 
#	the k-th generation of Tom's family tree (don't count the Aa Bb mates at
#	each level). Assume that Mendel's second law holds for the factors.

import sys
import math

with open(sys.argv[1]) as infile:
	k,  n = [int(x) for x in infile.readline().strip().split()]
	
def binomial(n, k):
	if n == 0 or k == 0:
		return 1
	else:
		return math.factorial(n)/(math.factorial(k) * math.factorial(n - k))
	
prob = 0	
for i in range(n):
	prob += binomial(2**k, i) * 0.25**i * 0.75**(2**k - i)
	
print "%.3f" % (1 - prob)

#Tom is heterozygous, and will mate with a heterozygote to have 2 kids
#k = generations of Tom
#n = number of heterozygous children

# 2**k kids in the kth generation
# probability that at least n kids are heterozygous is 1-probability of none
# p(none recessive) = (0.75)**(2**k)

'''
AaBb = .5*.5	= 0.25  <-
AaBB = .5*.25	= 0.125
Aabb = .5*.25	= 0.125
AABB = .25*.25	= 0.0625
AABb = .25*.5	= 0.125
AAbb = .25*.25	= 0.0625
aaBB = .25*.25	= 0.0625
aaBb = .25*.5	= 0.125
aabb = .25*.25	= 0.0625
				= 1.0000
'''



#! /usr/bin/env python

# Longest Increasing Subsequence http://rosalind.info/problems/lgis/
# input: A positive integer n<=10000 followed by a permutation p of 
#	length n.
#output: A longest increasing subsequence of p, followed by a longest 
#	decreasing subsequence of p.

import sys

def findCeil(term, search_space, n):
	bottom = 0
	top = n
	
	while bottom + 1 != top:
		test = (top + bottom)/2
		if search_space[test] > term:
			top = test
		else:
			bottom = test
	if search_space[bottom] <= term:
		return bottom +1
	else:
		return -1
		
def findFloor(term, search_space, n):
	bottom = 0
	top = n
	
	while bottom + 1 != top:
		test = (top + bottom)/2
		if term < search_space[test]:
			bottom = test
		else:
			top = test
	if search_space[top] <= term:
		return bottom +1
	else:
		return -1

def Longest_Increasing(seq, n):
	T = [0] * n # temporary results marking the last index of seq in the subsequence with length of T[i]
	R = [-1] * n # finalized results tracing the subsequences, largest is in the last position of R thats not -1
	ln = 0
	
	for i in range(1,n):
		if seq[i] > seq[T[ln]]:
			ln += 1
			T[ln] = i
			R[i] = T[ln-1]
		elif seq[i] < seq[T[0]]:
			T[0] = i
		else:
			j = findCeil(seq[i], [seq[x] for x in T[:ln+1]], ln+1)
			T[j] = i
			R[i] = T[j-1]
	# assemble the subsequence
	subseq = []
	r = T[ln]
	while r != -1:
		subseq.insert(0, seq[r])
		r = R[r]
	return subseq
	
def Longest_decreasing(seq, n):
	T = [0] * n # temporary results marking the last index of seq in the subsequence with length of T[i]
	R = [-1] * n # finalized results tracing the subsequences, largest is in the last position of R thats not -1
	ln = 0
	
	for i in range(1,n):
		if seq[i] < seq[T[ln]]:
			ln += 1
			T[ln] = i
			R[i] = T[ln-1]
		elif seq[i] > seq[T[0]]:
			T[0] = i
		else:
			j = findFloor(seq[i], [seq[x] for x in T[:ln+1]], ln+1)
			T[j] = i
			R[i] = T[j-1]

	# assemble the subsequence
	subseq = []
	r = T[ln]
	while r != -1:
		subseq.insert(0, seq[r])
		r = R[r]
		
	return subseq
			

with open(sys.argv[1]) as infile:
	n = int(infile.readline().strip())
	seq = [int(x) for x in infile.readline().strip().split()]
	
print ' '.join([str(x) for x in Longest_Increasing(seq, n)])
print ' '.join([str(x) for x in Longest_decreasing(seq, n)])
	

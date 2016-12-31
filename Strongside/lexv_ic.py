#! /usr/bin/env python

# input: A permutation of at most 12 symbols defining an ordered alphabet 
#	A and a positive integer n (n<=4).
#output: All strings of length at most n formed from A, ordered 
#	lexicographically. (Note: As in "Enumerating k-mers Lexicographically", 
#	alphabet order is based on the order in which the symbols are given.)

import sys
import time
from itertools import product

def create_Dictionary(letters, length):
	dictionary = []
	for n in range(1,length+1):
		for word in product(letters, repeat=n):
			dictionary.append(''.join(word))
	return dictionary
	
def n_order(dictionary, alphabet, m):
	sub_dictionaries = {}
	for alpha in alphabet[:-1]:
		sub_dictionaries[alpha] = []
	
	print sub_dictionaries
	for i in range(len(dictionary)):
		time.sleep(0.1)
		for a in range(len(alphabet)-1):
			if alphabet[a] == dictionary[i][m]:
				sub_dictionaries[alphabet[a]].append(dictionary[i])
	
	for alpha in alphabet[:-1]:
		sub_dictionaries[alpha]
				
			

def main():
	with open(sys.argv[1]) as infile:
		alphabet = infile.readline().strip().split()
		n = int(infile.readline().strip())
	
	dictionary = create_Dictionary(alphabet, n)
	alphabet.append(' ')
	n_order(dictionary, alphabet, 0)
	print dictionary

if __name__ == '__main__':
	main()

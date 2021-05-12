#！/usr/bin/python
# DocDistance.py - initial version of document distance
#
# written by keming
#
# Usage:
# DocDistance.py filename1 filename2
import string

import math

import sys

def read_file(filename):
	"""
	read and return file content
	"""
	with open(filename, 'r', encoding='utf8') as f:
		text = f.read()
	return text
	
translate_table = str.maketrans(string.ascii_uppercase+string.punctuation, string.ascii_lowercase+' '*len(string.punctuation))
def split_content_into_words(text):
	"""
	parse the given text into words
	return list of all words found
	"""
	text = text.translate(translate_table)
	words_list = text.split()
	return words_list
	
def count_frequency(words_list):
	"""
	return dictionry mapping words to frequency
	"""
	D = {}
	for word in words_list:
		if word in D:
			D[word]+=1
		else:
		    D[word]=1
	return D
	
def word_frequency_from_file(filename):
	"""
	return dictionry of {word, frequency} pairs for the given file 
	"""
	text = read_file(filename)
	word_list = split_content_into_words(text)
	frequency_mapping = count_frequency(word_list)
	return frequency_mapping
	
	

def inner_product(D1, D2):
	"""
	return inner product between two vectors
	vector represent {word:frequency}
	"""
	sum = 0.0
	for key in D1:
		if key in D2:
			sum += D1[key]*D2[key]
	return sum

def vector_angle(D1, D2):
	"""
	return angle between two vectors
	"""
	numerator = inner_product(D1, D2)
	denominator = math.sqrt(inner_product(D1, D1)*inner_product(D2, D2))
	print(numerator/denominator)
	return math.acos(numerator/denominator)
	

def main():
	if len(sys.argv)!=3:
		print("Usage: DocDistace.py filename1 filename2")
	else:
		filename1 = sys.argv[1]
		filename2 = sys.argv[2]
		filename1_word_frequency = word_frequency_from_file(filename1)
		filename2_word_frequency = word_frequency_from_file(filename2)
		print(filename1_word_frequency)
		print(filename2_word_frequency)
		doc_dis = vector_angle(filename1_word_frequency, filename2_word_frequency)
		print("doc_dis: ", doc_dis)
		
		
		
if __name__ == "__main__":
	import profile
	profile.run("main()")
		
	























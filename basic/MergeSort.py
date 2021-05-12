#!/usr/bin/python
#
# written by keming
#
# Usage:
# InsertSort.py [4,3,2,1] 

import sys

def insert_sort(arr):
	"""
	insert sort implementation
	complexity: O(n**2)
	"""
	for i in range(1, len(arr)):
		key = arr[i]
		j = i-1
		while j >= 0 and arr[j] > key:
			arr[j+1] = arr[j]
			j -= 1
		arr[j+1] = key		
	return arr
	
	
if __name__ == "__main__":
	print(insert_sort([4,5,7,1,2,4,11,23,123,22,21,2222,22,4,5,321,312,5435,67,4,57,45]))
	
				
	
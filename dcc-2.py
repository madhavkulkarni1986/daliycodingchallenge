'''
Question: Day 2
[The below questions was asked at Uber interview]
Given an array of integers, return a new array such that each element at index i of the 
new array is the product of all the numbers in the original array except the one at i.

Example 1:
Input [1, 2, 3, 4, 5]
Output [120, 60, 40, 30, 24]. 

Example 2:
Input: [3, 2, 1]
Output: [2, 3, 6].

****** https://www.dailycodingproblem.com/ ****** 
'''

import sys
## In Python 3, reduce is moved to functools
from functools import reduce 

def usage():
	print("Argument missing or wrong numnber of arguments")
	print("Usage: {} \"<List of integers>\"".format(sys.argv[0]))
	print("   Example: {} \"1 2 3 4 5\"".format(sys.argv[0]))
	sys.exit()

def product_calculator(values):
	for v in values:
		val=list(values)
		val.remove(v)
		# final_arr2.append(reduce(lambda x,y: x*y,val,1))
		yield reduce(lambda x,y: x*y,val,1)

##############################
## Method 1: Using division ##
##############################

##Process the argument given in command line to extract the list items
values=list()
if(len(sys.argv) != 2):
	usage()

for i in sys.argv[1].split():
	values.append(int(i))

## Find the product of all the items in the list
## I use lambda and reduce function. This can also achieved by other means, like iterative method.
product=reduce(lambda x,y: x*y, values,1)

result_list=[int(product/val) for val in values ]
print("Using division: {}".format(result_list))

######################################
## Method 2: Without using division ##
######################################

## The computation is done via generator functions
result=product_calculator(values)
## 'result' is a iteratable. You can also loop through to get individual items printed
print("Without using division:" + str(list(result)))
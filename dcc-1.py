'''
Question: Day 1
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

Example 1:
[10, 15, 3, 7] and k of 17
  return true, since 10 + 7 is 17.
Example 2:
[10, 15, 3, 7] and k=31
  return false, since no two numbers in the list add to 31

****** https://www.dailycodingproblem.com/ ****** 
'''
import sys

def usage():
	'''
	Print usage of the program
	'''
	print("Argument missing or wrong numnber of arguments")
	print("Usage: {} \"<List of integers>\" <K>".format(sys.argv[0]))
	print("   Example: {} \"1 2 3 4 5\" 7".format(sys.argv[0]))
	sys.exit()

values=list()
if(len(sys.argv) != 3):
	usage()


k=int(sys.argv[2])
##Process the argument given in command line to extract the list items
for i in sys.argv[1].split():
	values.append(int(i))

####################
## Logic:
##		- sort the given list
##		- initialize starting index and the last index to variables
##		- start traversing the list using the above indices and compare their sum to k
##		- if they match, set flag to true
##		- else, depending on greater than k or less than k, decrement right index or increment left index, respectively
####################
values.sort()
l_index=0
r_index=len(values)-1
flag="False"

while(l_index < r_index):
	if(values[l_index] + values[r_index] == k):
		flag="True"
		break
	elif(values[l_index] + values[r_index] < k):
		l_index+=1
	else:
		r_index-=1
print(flag)
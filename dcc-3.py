'''
Question: Day 3
[The below questions was asked at Uber interview]
Given the root to a binary tree, implement serialize(root),which serializes the tree into a string,
and deserialize(s), which deserializes the string back into the tree.

Example:

Given the following node:
	node = Node('root', Node('left', Node('left.left')), Node('right'))

Input:
	deserialize(serialize(node)).left.left.val)
Output:
	left.left

****** https://www.dailycodingproblem.com/ ****** 
'''
class Node:
	'''
	Node class for the binary tree
	'''
	def __init__(self,value,left=None,right=None):
		self.value=value
		self.left=left
		self.right=right

def serialize(node):
	'''
	Serialize the give binary tree. We us pre-order(Root, Left, Right) tree traversal here
	hash(#) is the place holder for child of leaf nodes. This is necessary to indicate leaf node when
	we are reconstructing the tree(deserialization).
	'''
	def shelper(node):
		if(not node):
			flattened_tree.append('#')
			return

		flattened_tree.append(node.value)
		shelper(node.left)
		shelper(node.right)

	flattened_tree=list()
	shelper(node)

	return flattened_tree

def deserialize(flattened_tree):
	'''
	Deserialize the list passed as parameter
	'''
	def helper():
		for val in vals:		
			if(val == "#"):
				return None

			node=Node(val)
			node.left=helper()
			node.right=helper()
			return node

	vals=iter(flattened_tree)
	return helper()

# Construct the tree
# node = Node('root', Node('left', Node('left.left')), Node('right'))
node = Node('root', Node('left', Node('left.left'),Node('left.right')), Node('right',right=Node('right.right')))

# The above tree looks as below:
#   		 root
#		    /	 \
#		 left    right
#	    /    \       \ 
#	 left   right   right

try:
	print(deserialize(serialize(node)).left.left.value)
except AttributeError:
	print("Tree does not have the node specified")
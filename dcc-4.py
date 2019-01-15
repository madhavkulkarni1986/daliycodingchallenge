'''
Question: Day 4
Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

Example 1:
    Input: [3, 4, -1, 1]
    Output: 2

Example 2:
    Input: [1, 2, 0]
    Output: 3

****** https://www.dailycodingproblem.com/ ******
'''
def missing_num(lst):
    l = sorted(set(lst))
    try:
        i = l.index(1)
        sublst=l[i:]
        for x in range(len(sublst)):
            if(x+1 != sublst[x]):
                return x
        return len(sublst)+1
    except ValueError:
        return 1

lst1=[-4,-3,-7,-1,3,-2,2,1,6,8,9,0,7,4,5]
missn=missing_num(lst1)
print(missn) # prints 10
lst2=[1,]
missn=missing_num(lst2)
print(missn) # prints 2

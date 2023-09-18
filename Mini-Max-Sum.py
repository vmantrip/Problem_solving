"""
Given five positive integers, find the minimum and maximum values that can be 
calculated by summing exactly four of the five integers. 
Then print the respective minimum and maximum values as a single line of two space-separated long integers.
"""

def miniMaxSum(arr):
    # Write your code here
    my_arr = sorted(arr)
    print(f'The sorted array is {my_arr}')
    min_sum = sum(my_arr[0:len(my_arr)-1])
    max_sum = sum(my_arr[1:])
    print(f'Minimum sum of any 4 integers is {min_sum}. Maxmum sum of any four integers is {max_sum}')

import random
randomlist = []
for i in range(0,5):#Constraint: Input array has only 5 elements
    n = random.randint(1,5)
    randomlist.append(n)
print(f'Input array is {randomlist}')
miniMaxSum(randomlist)
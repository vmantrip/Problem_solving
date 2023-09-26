"""
Given an array of integers and a positive integer k, determine the number of (i,j) pairs where i<j and ar[i] + ar[j] 
is divisible by k.

Example

ar = [1,2,3,4,5,6]
k = 6

Three pairs meet the criteria: [1,4],[2,3] and [4,6].
"""

def divisibleSumPairs(n, k, ar):
    # Write your code here
    my_arr = sorted(ar)
    fin_count=0
    for i in range(len(my_arr)-1):
        for j in range(i+1, len(my_arr)):
            new_sum = my_arr[i]+my_arr[j]
            if new_sum%k==0:
                fin_count+=1
            else:
                continue
    return fin_count
"""
There is a large pile of socks that must be paired by color. 
Given an array of integers representing the color of each sock,
determine how many pairs of socks with matching colors there are.
"""
def sockMerchant(n, ar):
    # Write your code here
    my_dict={}
    for i in ar:
        if i not in my_dict:
            my_dict[i]=1
        else:
            my_dict[i]+=1
    pair_count=0
    for i in my_dict:
        pair_count+=my_dict[i]//2
    return pair_count

import random
randomlist = []
for i in range(0,10):
    n = random.randint(1,5)
    randomlist.append(n)
print(f'Socks list is {randomlist}')
fin_count = sockMerchant(randomlist)
print(f'Number of pairs of socks are {fin_count}')
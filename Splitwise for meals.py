"""
Complete the bonAppetit function in the editor below. It should print Bon Appetit if the bill is fairly split. Otherwise, it should print the integer amount of money that Brian owes Anna.

bonAppetit has the following parameter(s):

bill: an array of integers representing the cost of each item ordered
k: an integer representing the zero-based index of the item Anna doesn't eat
b: the amount of money that Anna contributed to the bill
"""
def bonAppetit(bill, k, b):
    # Write your code here
    total_sum=0
    for i in range(len(bill)):
        if i!=k:
            total_sum=total_sum+bill[i]
        else:
            continue
    total_sum=total_sum/2
    if total_sum==b:
        print('Bon Appetit')
    else:
        print(int(b-total_sum))

import random
randomlist = []
for i in range(0,5):#Constraint: Input array has only 5 elements
    n = random.randint(10,50)
    randomlist.append(n)
bonAppetit(randomlist,2, 90)
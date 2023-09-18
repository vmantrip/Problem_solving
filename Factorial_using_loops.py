"""
Calculate and print the factorial of a given integer.
"""
def Factorial(n):
    # Write your code here
    my_ans=1
    my_val=n
    while n>=1:
        my_ans*=n
        n-=1
    print(f'The factorial of {my_val} is {my_ans}.')

import random
randomlist = []
for i in range(0,5):#Constraint: Input array has only 5 elements
    n = random.randint(1,10)
    randomlist.append(n)
print(f'Input array is {randomlist}')
for i in randomlist:
    Factorial(i)
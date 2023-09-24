"""
Two children, Lily and Ron, want to share a chocolate bar. Each of the squares has an integer on it.

Lily decides to share a contiguous segment of the bar selected such that:

The length of the segment matches Ron's birth month, and,
The sum of the integers on the squares is equal to his birth day.
Determine how many ways she can divide the chocolate.
"""

def birthday(s, d, m):
    # Write your code here
    #sub list length = m = birth month
    #sub list sum = date =d
    bar_list1 = [int(i) for i in s]
    i=0
    j=m-1
    ans_count=0
    while j<=len(bar_list1)-1:
        sub_list = bar_list1[i:j+1]
        if sum(sub_list)==d:
            ans_count+=1
            i+=1
            j+=1
        else:
            i+=1
            j+=1
    return ans_count

a = int(input("Enter number of squares in chocolate bar"))
import random
randomlist = []
for i in range(0,a):
    n = random.randint(1,10)
    randomlist.append(n)
print(f'Choclate bar looks like {randomlist}')
randomlist1 = []
j=0
while j<2:
    if j==0:
        n = random.randint(1,30)
        randomlist1.append(n)
        j+=1
    else:
        n = random.randint(1,12)
        randomlist1.append(n)
        j+=1
print(f'Bith date is {randomlist1[0]}. Birth month is {randomlist1[1]}')
comb_possible = birthday(randomlist, randomlist1[0], randomlist1[1])
print(f'Number of posssibe chocolate divisions are: {comb_possible}')
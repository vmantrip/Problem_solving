"""
You are in charge of the cake for a child's birthday. 
You have decided the cake will have one candle for each year of their total age.
They will only be able to blow out the tallest of the candles. 
Count how many candles are tallest.
"""


def birthdayCakeCandles(candles):
    # Write your code here
    max_list = sorted(candles)
    no_count=0
    ans_count=1
    max_ret=max_list[len(candles)-1]
    counter=len(candles)-1
    if len(max_list)>1:
        while max_list[counter] == max_list[counter-1]:
            ans_count+=1
            counter-=1
            if counter==0:
                break
    else:
        ans_count=1
    return ans_count,max_ret

import random
randomlist = []
for i in range(0,10):
    n = random.randint(1,5)
    randomlist.append(n)
print(f'Candles array is {randomlist}')
print('Integers in above array represent height of candles.')
can_count, tallest_can = birthdayCakeCandles(randomlist)
print(f'The tallest candle is of length {tallest_can}, count of the tallest candle is {can_count}.')

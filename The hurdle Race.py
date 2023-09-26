"""
A video player plays a game in which the character competes in a hurdle race. 
Hurdles are of varying heights, and the characters have a maximum height they can jump. 
There is a magic potion they can take that will increase their maximum jump height by  unit for each dose. 
How many doses of the potion must the character take to be able to jump all of the hurdles. 
If the character can already clear all of the hurdles, return 0.

Example
height = [1,2,3,3,2]
k=1


The character can jump 1 unit high initially and must take 3-1=2 doses of potion to be able to jump all of the hurdles.
"""


def hurdleRace(k, height):
    # Write your code here
    min_dose=0
    max_jump=k
    for i in height:
        if i-max_jump>0:
            min_dose+=(i-max_jump)
            max_jump=max_jump+(i-max_jump)
        else:
            continue
    return min_dose

import random
randomlist = []
for i in range(0,10):
    n = random.randint(1,10)
    randomlist.append(n)
print(f'Hurdles look like {randomlist}')
dose_count = hurdleRace(1, randomlist)
print(f'Minimum dose to cross all hurdles is {dose_count}')

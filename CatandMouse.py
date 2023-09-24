"""
Cat and Mouse chase: 
You are given  queries in the form of x, y, and z representing the respective positions for cats A and B, and for mouse C.
Complete the function catAndMouse to return the appropriate answer to each query, which will be printed on a new line.

If cat A catches the mouse first, print Cat A.
If cat B catches the mouse first, print Cat B.
If both cats reach the mouse at the same time, print Mouse C as the two cats fight and mouse escapes.
"""
def catAndMouse(x, y, z):
    op_str=''
    if abs(z-x) < abs(z-y):
        op_str='Cat A'
    elif abs(z-x) > abs(z-y):
        op_str='Cat B'
    else:
        op_str='Mouse C'
    return op_str

import random
randomlist = []
for i in range(0,10):
    n = random.randint(-10,10)
    randomlist.append(n)

print(f'List is {randomlist}')
x = randomlist[2]
y = randomlist[5]
z = randomlist[7]
print(f'Positions are: CatA: {x}, CatB: {y}, MouseC:{z}') 
output=catAndMouse(x, y, z)
print(f'So the winner of chase is {output}')
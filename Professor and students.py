"""
A Discrete Mathematics professor has a class of students. 
Frustrated with their lack of discipline, the professor decides to cancel class if fewer than some number of students are present when class starts.
Arrival times go from on time (arrivalTime<=0) to arrived late (arrivalTime>0).

Given the arrival time of each student and a threshhold number of attendees, determine if the class is cancelled.
"""


def angryProfessor(k, a):
    # Write your code here
    fin_count=0
    for i in a:
        if i<=0:
            fin_count+=1
        else:
            continue
    if fin_count>=k:
        return 'YES'
    else:
        return 'NO'
    
import random
randomlist = []
for i in range(0,10):
    n = random.randint(-3,5)
    randomlist.append(n)
print(f'Ariival times list is {randomlist}')
print('Integers in above array represent arrival time difference of students.')
q = random.randint(0,5)
print(f'Professor asked {q} students to be on time.')
result = angryProfessor(q, randomlist)
if result=='YES':
    print('Professor took class.')
else:
     print('Professor cancelled the class.')
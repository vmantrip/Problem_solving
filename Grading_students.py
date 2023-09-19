"""
HackerLand University has the following grading policy:

Every student receives a  in the inclusive range from  to .
Any  less than  is a failing grade.
Sam is a professor at the university and likes to round each student's  according to these rules:

If the difference between the grade and the next multiple of 5 is less than 3, round grade up to the next multiple of 5.
If the value of grade is less than 38, no rounding occurs as the result will still be a failing grade.
"""

def gradingStudents(grades):
    # Write your code here
    new_answer=0
    final_answer=[]
    for i in grades:
        my_rem = i%5
        if i>=38:
            if my_rem>=3:
                new_answer = i+(5-my_rem)
            else:
                new_answer = i
        else:
            new_answer = i
        final_answer.append(new_answer)
    return final_answer

import random
randomlist = []
for i in range(0,5):#Constraint: Input array has only 5 elements
    n = random.randint(1,100)
    randomlist.append(n)
print(f'Input array is {randomlist}')
response = gradingStudents(randomlist)
print(f'Graded array is {response}')
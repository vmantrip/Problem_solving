"""
Given a square matrix, calculate the absolute difference between the sums of its diagonals.
"""


def diagonalDifference(arr):
    # Write your code here
    i,j=0,0
    lt_arr = len(arr)
    sum1=0
    sum2=0
    while j<=len(arr)-1:
        sum1 += arr[i][j]
        sum2 += arr[i][len(arr)-(i+1)]
        i+=1
        j+=1
    return abs(sum2-sum1)

n = int(input('Enter the size of your square matrix.'))

arr = []

for _ in range(n):
    print(f'Enter {n} single spaced inputs for row number { _ + 1}.')
    arr.append(list(map(int, input().rstrip().split())))
result = diagonalDifference(arr)
print(f'The absolute difference between principal diagonals is {result}')
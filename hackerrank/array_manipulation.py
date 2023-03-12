#https://www.hackerrank.com/challenges/crush/problem?isFullScreen=true

# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulation(n, queries):
    # Write your code here
    arr = [0]*n
    for query in queries:
        a = query[0]-1
        b = query[1]
        for j in range(a,b):
            arr[j] += query[2]
    return max(arr)
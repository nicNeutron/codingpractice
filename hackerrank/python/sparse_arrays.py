#https://www.hackerrank.com/challenges/sparse-arrays/problem?isFullScreen=true

#
# Complete the 'matchingStrings' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY stringList
#  2. STRING_ARRAY queries
#

def matchingStrings(stringList, queries):
    # Write your code here
    hashmap = {}
    result = []
    for string in stringList:
        if string in hashmap:
            hashmap[string] += 1
        else:
            hashmap[string] = 1
    for query in queries:
        if query in stringList:
            result.append(hashmap[query])
        else:
            result.append(0)
    return result


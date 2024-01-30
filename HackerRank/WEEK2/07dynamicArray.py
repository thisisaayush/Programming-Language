#!/bin/python3

# Complete the 'dynamicArray' function below.
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries

def dynamicArray(n, queries):
    seqList = [[] for _ in range(n)]
    lastAnswer = 0
    answers = []

    for query in queries:
        query_type, x, y = query
        index = (x ^ lastAnswer) % n

        if query_type == 1:
            seqList[index].append(y)
        elif query_type == 2:
            lastAnswer = seqList[index][y % len(seqList[index])]
            answers.append(lastAnswer)

    return answers

if __name__ == '__main__':
    # Read the input line containing 'n' and 'q'
    n, q = map(int, input().strip().split())

    queries = []

    for _ in range(q):
        # Read the input line containing 'query_type', 'x', and 'y'
        query = list(map(int, input().strip().split()))
        queries.append(query)

    result = dynamicArray(n, queries)

    # Print the output to the standard output
    for item in result:
        print(item)

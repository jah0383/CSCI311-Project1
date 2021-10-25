def editDistance(word1: str, word2: str) -> int:
    """Given two strings word1 and word2.
    Return the minimum number of operations (insert, delete, replace) required to convert word1 to word2
    
    Runtime: O(m x n)"""
    subproblems = [ [float("inf")] * (len(word2) + 1) for i in range(len(word1) + 1)]

    #Establish Base Case
    for j in range(len(word2) + 1):
        subproblems[len(word1)][j] = len(word2)-j
    for i in range(len(word1) + 1):
        subproblems[i][len(word2)] = len(word1)-i

    for i in reversed(range(len(word1))):
        for j in reversed(range(len(word2))):
            if word1[i] == word2[j]:
                subproblems[i][j] = subproblems[i+1][j+1]
            else:
                #Check previous subproblem calculations
                deletion = subproblems[i+1][j]
                insertion = subproblems[i][j+1]
                replace = subproblems[i+1][j+1]
                #Set to 1 + minimum
                subproblems[i][j] = min(deletion, insertion, replace) + 1

    return subproblems[0][0]

# from pandas import *

# def printSubProblems(subproblems, word1, word2):
#     df = DataFrame(subproblems)
#     df.set_axis(list(word1+' '),axis=0)
#     df.set_axis(list(word2+' '),axis=1)
#     print(df)


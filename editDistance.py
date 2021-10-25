# from pandas import *

# def printSubProblems(cache, word1, word2):
#     df = DataFrame(cache)
#     df.set_axis(list(word1+' '),axis=0)
#     df.set_axis(list(word2+' '),axis=1)
#     print(df)


def editDistance(word1: str, word2: str) -> int:
    """Given two strings word1 and word2.
    Return the minimum number of operations (insert, delete, replace) required to convert word1 to word2"""
    cache = [ [float("inf")] * (len(word2) + 1) for i in range(len(word1) + 1)]

    #Establish Base Case
    for j in range(len(word2) + 1):
        cache[len(word1)][j] = len(word2)-j
    for i in range(len(word1) + 1):
        cache[i][len(word2)] = len(word1)-i

    # printSubProblems(cache,word1,word2)

    for i in reversed(range(len(word1))):
        for j in reversed(range(len(word2))):
            if word1[i] == word2[j]:
                cache[i][j] = cache[i+1][j+1]
            else:
                #Check previous subproblem calculations
                deletion = cache[i+1][j]
                insertion = cache[i][j+1]
                replace = cache[i+1][j+1]
                #Set to 1 + minimum
                cache[i][j] = min(deletion, insertion, replace) + 1

    # printSubProblems(cache, word1,word2)
    return cache[0][0]
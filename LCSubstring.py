def LCS(D, t):

    # Length of dna sequence string (D) and query sequence string (t)
    len1 = len(D)
    len2 = len(t)

    # Create a lookup table, table[i][j], based on length of strings to store the lengths of substrings.
    # i.e. creating an empty m * n table. Added extra row and column because our values depend on diagonals.
    table = [[0 for y in range(len2 + 1)] for x in range(len1 + 1)]

    # largest common substring length
    maxLCS = 0
    # index of our maxLen, this will indicate the end of our LCS         
    index = len1

    # Fill table by iterating through both strings with lengths of substrings
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):

            # Check if current characters D and t equal.
            # If they do, set the current table value to left diagonal value + 1, this take the  left diagonal
            # of the current table value and adds 1 to this substring length.
            # If the previous letters were not the same, the diagonal will be 0 giving 1.
            if D[i - 1] == t[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1

                # Check if our current substring is the max length if it is set our new i to the index of that max
                # substring length and set our new longest common substring
                if table[i][j] > maxLCS:
                    index = i
                    maxLCS = table[i][j]

    # Takes the end index of our LCS and minus that from max LCS length, this gives us the starting index for our LCS.
    # Then we take the slice from our original string and that gives us our LCS . We then return the longest common substring.
    startIndex = index - maxLCS
    endIndex = index
    LCS_VALUE = D[startIndex: endIndex]
    return LCS_VALUE

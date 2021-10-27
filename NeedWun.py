# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 13:54:26 2021

@author: James Howe
"""


def NWA(s1, s2, MMI_scoring = (1,-1,-1),debug = False):
    m = len(s1) + 1
    n = len(s2) + 1
    
    match_score = MMI_scoring[0]
    mismatch_score = MMI_scoring[1]
    indel_score = MMI_scoring[2]

    #setting up the table 
    cost_table = [[0 for i in range(m)] for j in range(n)]
    #Setting first row to be 0,-1,-2.....
    for i in range(1,m):
        cost_table[0][i] = cost_table[0][i-1] + indel_score
    #Setting first row to be Transpose[0,-1,-2.....]
    for i in range(1,n):
        cost_table[i][0] = cost_table[i-1][0] + indel_score

    #funky diagonal matrix 
    for k in range(1,m+n):
        start_col = max(1, k - n)
        count = min(k, (m - start_col), n)
        for r in range(0,count):
            i = min(n, k) - r - 1
            j = start_col + r
            
            #Don't look at the first row
            if(i==0):
                break

            match = (s1[j-1]==s2[i-1])

            costs = [0,0,0]
            #indel top cost
            costs[0] = cost_table[i-1][j] + indel_score
            #indel left cost 
            costs[1] = cost_table[i][j-1] + indel_score
            #match or mismatch cost
            if(match):
                costs[2] = cost_table[i-1][j-1] + match_score
            else:
                costs[2] = cost_table[i-1][j-1] + mismatch_score
        
            if(debug):
                print_table_nice(cost_table,i,j,s1,s2)
                
            cost_table[i][j] = max(costs)

    if(debug):        
        print()
        print_table_nice(cost_table,i,j,s1,s2,False)
    return cost_table[n-1][m-1]

def print_table_nice(cost_table,i,j,s1,s2,pos = True):
    """
    This is just a function I made to help me debug the algorithm, it just
    prints out the current solutions table in a nice format
    """
    ct = cost_table.copy()
    if pos:
        ct[i][j] = "*"
        print()
        print(s1[j-1] + " " + s2[i-1])
        print(str(i) + " " + str(j))
    print("      ",end="")
    for x in s1:
        print("  " + x,end="")
    print()
    for xi, x in enumerate(ct):
        if xi != 0:
            print(s2[xi-1],end=" ")
        else:
            print("  ",end="")
        print("|",end="")
        for yi, y in enumerate(x):
            if y == "*":
                print("  *",end="")
            else:
                print("{:3}".format(y),end="")
        print("|")
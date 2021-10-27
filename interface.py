# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 15:12:36 2021

@author: James Howe
"""

import sys
import editDistance
import LCSubstring
import LCSubsequence
import NeedWun


#Handles all the algoirithm information 
cur_algo = 2
algo_dict = {0:"Longest common substring",
             1:"Longest common subsequence",
             2:"Edit Distance",
             3:"Needleman–Wunsch"}
NeedWun_scoring = [1,-1,-1]

query_file_path = "DNA_query.txt"
query_file = open(query_file_path, "r")
seq_file_path = "DNA_sequences.txt"
seq_file = open(seq_file_path, "r")


menu_page = 0
last_input = None

seq_list = []
query_string = "a"



def find_best_match():
    """
    Goes through each dna sequence and finds the one which matches the query 
    sequence the best given the current algorithm 
    """
    global cur_algo
    print("QS is:", query_string)
    print("Current algo:", algo_dict[cur_algo])
    min_result = sys.maxsize
    max_result = -1*sys.maxsize
    winner = -1
    golf_score = (cur_algo == 2) #Whether or not the algo uses low or high to mean similar
    for x in range(len(seq_list)):
        
        result = run_algo(query_string,seq_list[x][1],cur_algo)
        if type(result) == type("string"):
            result = len(result)
        print("({}/{})[{}] {}".format((x+1),len(seq_list),result,seq_list[x][0]))
        
        
        ##Since different algos use golf score and others don't
        if(golf_score):
            if result < min_result:
                min_result = result
                winner = x
        else:
            if result > max_result:
                max_result = result
                winner = x  


    if(golf_score):
        return winner, min_result  
    else:
        return winner, max_result        


def run_algo(s,t,n):
    """
    Takes in 2 strings and the currently selected algorithm and returns 
    whatever that algorithm returns 
    """
    if n == 0: # Longest common substring
        return LCSubstring.LCS(s,t)
    elif n == 1: #Longest common subsequence
        return LCSubsequence.LCS(s,t)
    elif n == 2: #Edit Distance
        return editDistance.editDistance(s,t)
    elif n == 3: 
        return NeedWun.NWA(s,t,NeedWun_scoring)

def parse_seq():
    """
    Reads in the sequence File and puts each sequence into a list
    """
    global seq_list
    seq_content = open(seq_file_path, "r").read()
    seq_content = seq_content.strip().split(">")
    seq_content = [i.split("\n") for i in seq_content[1:]]
    seq_list = []
    for x in seq_content:
        seq_list.append((x[0].upper(),"".join(x[1:])))

    
def parse_query():
    """
    Reads in the query file and puts it into a string
    """
    global query_string
    qs = open(query_file_path, "r").read()
    qs = qs.strip().upper()
    query_string = qs
    

def print_main_menu():
    """
    Prints the main menu, handling all the style and formating, no real logic 
    is done here 
    """
    print(("""
    Current query file: {}
    Current seq file:   {}
    Current algo:       {}
    """).format(query_file_path,seq_file_path,algo_dict[cur_algo]),end="")
    if(cur_algo == 3):
        print(("""Current Needleman–Wunsch scoring is 
            Match    : {:^3} 
            MisMatch : {:^3} 
            Indel    : {:^3}""").format(*NeedWun_scoring))
    print("""--------------------------------------------------------
    OPTIONS
    1: Set files
    2: Choose algo
    3: Run algo""")
    
    if(cur_algo == 3):
        print("    4: Change Needleman–Wunsch scoring")
    
    print("    0: Quit")

        
def get_file_names():
    """
    Gets the name of the files from the user
    """
    global query_file_path, query_file, seq_file_path, seq_file
    print("Current query file:", query_file_path)
    print("What's the name of the file which contains the query?")
    file_name = input()
    while True:
        try:
            query_file = open(file_name, "r")
            query_file_path = file_name
            print("Succsefully changed file!")
            break
        except Exception as e:
            print(e)
            print("Sorry something went wrong please input the file name again")
            file_name = input()
    
    print("Current seq file:", seq_file_path)
    print("What's the name of the file which contains the sequences?")
    file_name = input()
    while True:
        try:
            seq_file = open(file_name, "r")
            seq_file_path = file_name
            print("Succsefully changed file!")
            break
        except Exception as e:
            print(e)
            print("Sorry something went wrong please input the file name again")
            file_name = input()
            
def change_algo():
    """
    Changes the algorithm to one that the user decides on 
    """
    global cur_algo
    print("Current algo:", algo_dict[cur_algo])
    #print options


    while True:
        for a in algo_dict.keys():
                print(("{}: {}").format(a,algo_dict[a]))
        print("Please choose an algorithm")
        try:
            algo_choice = int(input())
            if algo_choice in algo_dict.keys():
                break
            else:
                print("input not understood or not a valid choice, try again")
        except Exception as e:
            print(e)
            print("Please input again")
    cur_algo = algo_choice

if __name__ == "__main__":
    """
    The main loop of the code, gets user input and shows relevent information
    """
    while True:
        #Every loop go reparse the seq and query file to make sure they are up to date
        parse_seq()
        parse_query()
        if menu_page == 0:
            
            print_main_menu()
            while True:
                last_input = input()
                if last_input == "0":
                    print("Bye!\n")
                    sys.exit(0) 
                elif last_input == "1":
                    menu_page = 1
                    break
                elif last_input == "2":
                    menu_page = 2
                    break
                elif last_input == "3":
                    menu_page = 3
                    break
                elif last_input == "4" and cur_algo == 3:
                    menu_page = 4
                    break
                else:
                    print("not a page option")
            
        elif menu_page == 1:
            print()
            get_file_names()
            menu_page = 0
        elif menu_page == 2:
            print()
            change_algo()
            menu_page = 0
        elif menu_page == 3:
            print()
            winner, min_result = find_best_match()
            print("The closest DNA sequence is '{}'!".format(seq_list[winner][0]))
            print("With similarity score of {}!".format(min_result))
            temp = input()
            menu_page = 0
        elif menu_page == 4:
            print("Please input 3 numbers seperated by commas")
            
            while True:
                last_input = input()
                try:
                    NeedWun_scoring = last_input.split(",")
                    NeedWun_scoring = [int(i) for i in NeedWun_scoring]
                    break;
                except Exception as e:
                    print(e)
                    print("please try again")
            menu_page = 0
        else:
            print("whoops")
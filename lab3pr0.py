'''Name: Ben Gertz
    Course: CMPS 1500
    Lab Section: Tuesday 5-6.15 PM
    Assignment: Lab 3 Part 0
    Date: 09/25/2017
    This program contains the functions necessary for part two. The function add adds an indel at a specified position within a string.
    The function delete deletes an indel at a given position if there is an indel at that position and if there is not then it returns the string unchanged.
    The function validDNA checks to see if a string has only the letters A, T, G, and C. The function fill adds indels to the end of a string if its length
    is not as great as the entered length. The function score returns the amount of similar letters in two strings excluding indels.
    
'''

#functions
def add(string, position):
    string_new = ''
    for pos, char in enumerate(string):
        if position == pos:
            string_new += '-'
            string_new += char
        else:
            string_new += char
    if position == len(string):
        string_new += '-'
    else:
        pass
    return string_new

def delete(string, position):
    string_new = ''
    for pos, char in enumerate(string):
        if position == pos and char == '-':
            pass
        else:
            string_new += char
    return string_new

def validDNA(string):
    for char in string:
        if char not in 'ACTG':
            return False
        else:
            pass
    return True

def fill(string,n):
    if len(string) == n:
        pass
    else:
        string = string + ('-' * (n-len(string)))
    return string

def score(str1, str2):
    matches = 0
    if len(str1) > len(str2):
        fill(str2, len(str1))
    elif len(str1) < len(str2):
        fill(str1, len(str2))
    else:
        pass
    for pos, char in enumerate(str1):
        if char == str2[pos] and char != '-':
            matches += 1
        else:
            pass
    return matches

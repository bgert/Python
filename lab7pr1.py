''' Name: Ben Gertz
    Course: CMPS 1500
    Lab Section: Tuesday 5-6.15 PM
    Assignment: Lab 7 Part 1
    Date: 11/6/2017
    
'''

def uppercount(s):
    '''
    This function counts the number of uppercase letters in a string.
    input: string
    output: integer
    A real world application for this could be finding how many names are in a string because each first and
    last name will begin with a capital. Another use could be adapting the code to look for letters that will
    not transfer well between applications or operating systems like letters with accents.
    '''
    if len(s) == 0: #basecase
        return 0
    elif s[0] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ': #these two statements below are recursive
        return 1 + uppercount(s[1:])
    else:
        return 0 + uppercount(s[1:])

def clean_string(s):
    '''
    This function takes all characters out of a string that are not a space, uppercase letter, or lowercase letter.
    input: string
    output: string
    '''
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz '
    if len(s) == 0: #base case
        return ''
    if s[0] in letters: #these two statements below are recursive
        return s[0] + clean_string(s[1:])
    else:
        return clean_string(s[1:])

def clean_list(l1, l2):
    '''
    This function takes two lists and returns a list made of elements that were in l1 but not in l2.
    input l1: list
    input l2: list
    output: list
    '''
    if len(l1) == 0: #base case
        return []
    if l1[0] in l2: #these two statements below are recursive
        return clean_list(l1[1:], l2)
    else:
        return [l1[0]] + clean_list(l1[1:], l2)

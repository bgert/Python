''' Name: Ben Gertz
    Course: CMPS 1500
    Lab Section: Tuesday 5-6.15 PM
    Assignment: Lab 6 Part 1
    Date: 10/30/2017
    This program contains two functions, is_sorted(), which checks to see if a list is sorted in ascending order, and is_file_sorted(), which
    checks to see if the numbers in a file go in ascending order using is_sorted().
'''

def is_sorted(lst): #O(1)
    '''
    This function takes a list of numbers and returns True if it is sorted in increasing
    order or else returns False.
    input: list of integers -> boolean
    >>> listTrue = [-1, 2, 3]
    >>> listFalse = [0, 1, 4, 3]
    >>> listEmpty = []
    >>> is_sorted(listTrue)
    True
    >>> is_sorted(listFalse)
    False
    >>> is_sorted(listEmpty)
    False
    >>>
    '''
    if len(lst) == 0: #O(1)
        return False #O(1)
    elif len(lst) == 1: #O(1)
        return True #O(1)
    elif lst[0] <= lst[1]: #O(1)
        return is_sorted(lst[1:]) #O(n)
    else: #O(1)
        return False #O(1)

def is_file_sorted(filename): #O(1)
    '''
    This function examines a file and checks to see if the numbers on each line are in ascending order and returns True,
    otherwise it returns False.
    input: strings from a file -> boolean
    '''
    int_list = [] #O(1)
    f = open(filename, 'r') #O(1)
    string_list = f.readlines() #O(n)
    f.close() #O(1)
    if string_list[0] == '\n': #O(1)
        return False #O(1)
    for num in range(len(string_list)): #O(n)
        int_list.append(int(string_list[num])) #O(n)
    return is_sorted(int_list) #O(n)

filename = input('Please enter file name:') #O(1)
if is_file_sorted(filename): #O(n)
    print('Congratulations! The file', filename, 'is nicely sorted!') #O(1)
else: #O(1)
    print('Looks like', filename, 'needs to be sorted') #O(1)
'''
    The total asymptotic runtime of my program is O(n). This is because every step that is repeated is
    only repeated n number of times so when added the constant is dropped and so are all the O(1)'s so
    O(n) is the dominant variable.
'''


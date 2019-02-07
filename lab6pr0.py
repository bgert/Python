''' Name: Ben Gertz
    Course: CMPS 1500
    Lab Section: Tuesday 5-6.15 PM
    Assignment: Lab 6 Part 0
    Date: 10/30/2017
    This program contains two functions, is_sorted(), which checks to see if a list is sorted in ascending order, and is_file_sorted(), which
    checks to see if the numbers in a file go in ascending order using is_sorted().
'''

def is_sorted(lst):
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
    if len(lst) == 0:
        return False
    elif len(lst) == 1:
        return True
    elif lst[0] <= lst[1]:
        return is_sorted(lst[1:])
    else:
        return False

def is_file_sorted(filename):
    '''
    This function examines a file and checks to see if the numbers on each line are in ascending order and returns True,
    otherwise it returns False.
    input: strings from a file -> boolean
    '''
    int_list = []
    f = open(filename, 'r')
    string_list = f.readlines()
    f.close()
    if string_list[0] == '\n':
        return False
    for num in range(len(string_list)):
        int_list.append(int(string_list[num]))
    return is_sorted(int_list)


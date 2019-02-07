'''Name: Ben Gertz
    Course: CMPS 1500
    Lab Section: Tuesday 5-6.15 PM
    Assignment: Lab 3 Part 1
    Date: 09/25/2017
    This program allows a user to enter two DNA sequences then prompts the user to select an option for what to do with those sequences. One option is to add an indel to some point in either sequence,
    the second is to delete an indel at some point in either sequence, the third is to score the amount of matching letters in each position excluding indels, and the fourth is to quit the program. 
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

#calculations
dna1 = input('Please enter the first \'biological\' string:\n') #This section asks for two DNA sequences, prompting the user again if the sequence is not DNA like
while validDNA(dna1) == False:
    dna1 = input('Please enter the first \'biological\' string:\n')
dna2 = input('Please enter the second \'biological\' string:\n')
while validDNA(dna2) == False:
    dna2 = input('Please enter the second \'biological\' string:\n')
print('String 1:', dna1, '\nString 2:', dna2)
choice = input('Select one of the following commands:\n\'a\' to add an indel\n\'d\' to delete an indel\n\'s\' to score the present alignment\n\'q\' to quit the program\n')
while choice not in 'adsq': #Makes sure that the user actually enters an allowed input
    choice = input('Select one of the following commands:\n\'a\' to add an indel\n\'d\' to delete an indel\n\'s\' to score the present alignment\n\'q\' to quit the program\n')
while choice != 'q': #makes sure that the user has not quit the program
    if choice == 'a':
        choice_a = input('Work on which string (1 or 2):\n')
        position_indel = int(input('Enter the position of the indel:\n'))
        if choice_a == '1': 
            dna1 = add(dna1, position_indel)
            print('Here\'s the result:', dna1)
        elif choice_a == '2':
            dna2 = add(dna2, position_indel)
            print('Here\'s the result:', dna2)
        else:
            pass
    elif choice == 'd':
        choice_d = input('Work on which string (1 or 2):\n')
        position_indel = int(input('Enter the position of the indel:\n'))
        if choice_d == '1':
            dna1 = delete(dna1, position_indel)
            print('Here\'s the result:', dna1)
        elif choice_d == '2':
            dna2 = delete(dna2, position_indel)
            print('Here\'s the result:', dna2)
        else:
            pass
    else:
        matches = score(dna1, dna2)
        print('There are', matches, 'matches')
    print('String 1:', dna1, '\nString 2:', dna2)
    #retrieves user's next choice of what to do with the two DNA sequences, again making sure its an allowed option
    choice = input('Select one of the following commands:\n\'a\' to add an indel\n\'d\' to delete an indel\n\'s\' to score the present alignment\n\'q\' to quit the program\n')
    while choice not in 'adsq': 
        choice = input('Select one of the following commands:\n\'a\' to add an indel\n\'d\' to delete an indel\n\'s\' to score the present alignment\n\'q\' to quit the program\n')
print('Bye!')
    

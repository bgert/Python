'''Name: Ben Gertz and Josh Shawver-Weiner
    Course: CMPS 1500
    Lab Section: Tuesday 5-6.15 PM
    Assignment: Lab 2 Part 2
    Date: 09/17/2017
    This program lets a user enter as many passwords as they want then displays them as a list, and displays them as
    a list of asterisks with the same length as the user entered password.
'''
#These next three lines define variables and a list used later in the program
password_list = []
ast_list = []
password = 'asdf'
while len(password) > 0:
    #input
    password = input('Please enter a password (press [enter] to finish): ')
    #Because the while loop checks the length of the statement before the user enters it there must be another if else statement to make sure the empty input the user enters to signal the end of the list is not added to the list.
    #computations
    if len(password) > 0: 
        password_list.append(password)
    else:
        break
#output
for index in password_list:
    ast_list.append('*' * len(index))
print(password_list)
print(ast_list)

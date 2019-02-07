'''Name: Ben Gertz and Josh Shawver-Weiner
    Course: CMPS 1500
    Lab Section: Tuesday 5-6.15 PM
    Assignment: Lab 2 Part 1
    Date: 09/17/2017
    This program checks to see if a password entered by the user is between 8 and 20 characters,
    has an uppercase letter, a lowercase letter, a number, a special character, and no spaces.
'''
valid = False #These variables are needed to check the type of character entered in the password
upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower_case = 'abcdefghijklmnopqrstuvwxyz'
number = '1234567890'
special_char = '”!?,.;:$#_&”'
space = ' '
while valid == False:
#input
    user_pass = input('Please enter a password:\n')
#calculations
    if len(user_pass) > 7 and len(user_pass) < 21:
        pass
    else:
        continue
    for char in space: #This sequence which is repeated to check for every parameter except length checks to see if the password entered by the user meets the criteria for acceptance.
        if char in user_pass:
            isspace = True
            break
        else:
            isspace = False
    for char in upper_case:
        if char in user_pass:
            upper = True
            break
        else:
            upper = False
    for char in lower_case:
        if char in user_pass:
            lower = True
            break
        else:
            lower = False
    for char in number:
        if char in user_pass:
            isnumber = True
            break
        else:
            isnumber = False
    for char in special_char:
        if char in user_pass:
            special = True
            break
        else:
            special = False
    if upper and lower and isnumber and special and not isspace:
        valid = True
    else:
        pass
#output
print('Password accepted')

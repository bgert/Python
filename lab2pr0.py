'''Name: Ben Gertz and Josh Shawver-Weiner
    Course: CMPS 1500
    Lab Section: Tuesday 5-6.15 PM
    Assignment: Lab 2 Part 0
    Date: 09/13/2017
    This program takes the first letter of every word, and all punctuation in a phrase and turns it into a password which is outputted to the user.
    Additionally, it changes a to @, o to 0, and l to 1.
'''
#input
phrase = input('Please enter a phrase: ')
#calculations
password = phrase[0] #Makes sure the first character is added to the password
char= ''
for pos, char in enumerate(phrase):
    if char in ",.!?;:":
        password += char
    elif char == ' ':
        post_space = str(phrase[pos + 1])
        if post_space not in ",.!?;:": #makes sure that the character after the space which would begin a new word is not also a special character
            if post_space in "oal": #changes o, a, and l to 0, @, and 1
                if post_space == 'o':
                    post_space ='0'
                elif post_space == 'a':
                    post_space = '@'
                elif post_space == 'l':
                    post_space = '1'
                else:
                    continue
            password += post_space
        else:
            continue
    else:
        continue
#output
print(password)

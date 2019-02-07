''' Name: Ben Gertz
    Course: CMPS 1500
    Lab Section: Tuesday 5-6.15 PM
    Assignment: Lab 4 Part 0-1
    Date: 10/2/2017
    This program creates a dictionary from a text file of people and their majors and also allows them to perform other functions on the dictionary. Finally it saves the dictionary to the file.
    get_menu_chioce(), get_menu_choice(str) -> int, this function gives a user choices for action, prompts a user to enter a choice, and returns the choice as an integer.
    display(d), display(str) -> str, this function prints the name and major of everyone in the dictionary.
    look_up(d), look_up(str) -> str, this program takes a given dictionary and asks for a key in it and returns the value, if the key is not in the dictionary it says so.
    add(d), add(str) -> str, this program takes a given dictionary and adds a key and a value to it, if the key is already present it says so.
    change(d), change(str) -> str, this program takes a given dictionary and asks for a key to change its value, if the key does not exists it says so.
    delete(d), delete(str) -> str, this program takes a given dictionary and asks for a key and deletes it from the dictionary, if it is not there it says so.
'''
import sys
## look_up 
def look_up(d):
    name = input('Enter a name: ')
    if name in d:
        print(d[name])
    else:
        print('Not Found.')

## add
def add(d):
    name = input('Enter a name: ')
    maj = input('Enter a major: ')
    if name in d:
        print('A person with this name already exists in the system.')
    else:
        d[name] = maj

## change 
def change(d):
    name = input('Enter a name: ')
    if name not in d:
        print('That name is not found')
    else:
        maj = input('Enter the new major: ')
        d[name] = maj

## delete 
def delete(d):
    name = input('Enter a name: ')
    if name in d:
        del d[name]
    else:
        print('That name is not found.')

## display 
def display(d):
    for key in d:
        print(key, 'is a wizard in', d[key])

## get_menu_choice 
def get_menu_choice():
    print('Majors of College Students\n---------------------------\n1. Look up a student\'s major\n2. Add a new major\n3. Change a major\n4. Delete a major\n5. Display all students\n6. Quit the program')
    valid_choice = ['1', '2', '3', '4', '5', '6']
    choice = input('Enter your choice: ')
    while choice not in valid_choice:
        choice = input('Enter a valid choice: ')
    return int(choice)
## open and read in dictionary
def dict_in(d):
    while True:
        try:
            f = open('input.txt', 'r')
            break
        except FileNotFoundError:
            print('File name does not exist. Create file \'input.txt\' and restart program')
            sys.exit()
    line_blank = f.read()
    if line_blank == '':
        return
    else:
        for line in f:
            line = line.rstrip()
            line = line.split('#')
            d[line[0]] = line[1]
    f.close()
def dict_out():
    f = open('input.txt', 'w')
    for key in majors:
        f.write(key + '#' + majors[key] + '\n')
    f.close()
## The main part of your program
majors = {}
choice = 0
dict_in(majors)
while choice != 6:
        choice = get_menu_choice()
        if choice == 1:
            look_up(majors)
        elif choice == 2:
            add(majors)
        elif choice == 3:
            change(majors)
        elif choice == 4:
            delete(majors)
        elif choice == 5:
            display(majors)
        dict_out()

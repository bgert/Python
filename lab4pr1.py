'''Name: Ben Gertz
    Course: CMPS 1500
    Lab Section: Tuesday 5-6.15 PM
    Assignment: Lab 4 Part 1
    Date: 10/2/2017
    This file contains functions for use in the program for lab four relating to dictionaries.
    get_menu_chioce(), get_menu_choice(str) -> int, this function gives a user choices for action, prompts a user to enter a choice, prints the choice and returns the choice as an integer.
    display(d), display(str) -> str, this function prints the name and major of everyone in the dictionary.
'''
majors = {'Harry': 'Computer Science', 'Hermione': 'Mathematics', 'Ron': 'English'}
def get_menu_choice():
    print('Majors of College Students\n---------------------------\n1. Look up a student\'s major\n2. Add a new major\n3. Change a major\n4. Delete a major\n5. Display all students\n6. Quit the program')
    valid_choice = ['1', '2', '3', '4', '5', '6']
    choice = input('Enter your choice: ')
    while choice not in valid_choice:
        choice = input('Enter a valid choice: ')
    return int(choice)
def display(d):
    for key in d:
        print(key, 'is a wizard in', d[key])

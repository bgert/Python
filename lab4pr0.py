'''Name: Ben Gertz
    Course: CMPS 1500
    Lab Section: Tuesday 5-6.15 PM
    Assignment: Lab 4 Part 0
    Date: 10/2/2017
    This program contains functions that are used in working with a dictionary containing people and their majors.
    look_up(d), look_up(str) -> str, this program takes a given dictionary and asks for a key in it and returns the value, if the key is not in the dictionary it says so.
    add(d), add(str) -> str, this program takes a given dictionary and adds a key and a value to it, if the key is already present it says so.
    change(d), change(str) -> str, this program takes a given dictionary and asks for a key to change its value, if the key does not exists it says so.
    delete(d), delete(str) -> str, this program takes a given dictionary and asks for a key and deletes it from the dictionary, if it is not there it says so.
'''
majors = {'Harry': 'Computer Science', 'Hermione': 'Mathematics', 'Ron': 'English'}

def look_up(d):
    name = input('Enter a name: ')
    if name in d:
        print(d[name])
    else:
        print('Not Found.')

def add(d):
    name = input('Enter a name: ')
    maj = input('Enter a major: ')
    if name in d:
        print('A person with this name already exists in the system.')
    else:
        d[name] = maj
def change(d):
    name = input('Enter a name: ')
    if name not in d:
        print('That name is not found')
    else:
        maj = input('Enter the new major: ')
        d[name] = maj
def delete(d):
    name = input('Enter a name: ')
    if name in d:
        del d[name]
    else:
        print('That name is not found.')

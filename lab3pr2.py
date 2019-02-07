'''Name: Ben Gertz
    Course: CMPS 1500
    Lab Section: Tuesday 5-6.15 PM
    Assignment: Lab 3 Part 2
    Date: 09/25/2017
    This program asks for a file name, reads the numbers on each line of that file, multiplies them together to find area,
    then adds all those togther to find the total area of all the rooms in the house.
'''
#function
def area(w, h):
    w = int(w)
    h = int(h)
    area = w * h
    return area
#input
file_name = input('Please enter file name:')
#open file
f = open(file_name, 'r')
#reorganize text
area_total = 0
for line in f:
    line = line.rstrip() #takes the \n implied at the end of each line to make a new line out of the string
    line = line.split(' ') #turns the string into a list
    area_total += area(line[0], line[1]) #counter to add calculated area to the previous total
f.close()
print('The calculated area is:', area_total)

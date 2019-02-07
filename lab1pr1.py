"""Name: Ben Gertz
    Course: CMPS 1500
    Lab Section: Tuesday 5:00- 6:15 PM
    Assignment: Lab 1 Part 1
    Date: 09/10/2017
 """
#input
us_Date = input('Please enter date in MM/DD/YYYY format: ')
#calculations
'''
This section determines the placement of the /'s in the user input in order
to determine where to take the numbers for the date.
'''
MM = us_Date[0] if us_Date[1] == '/'  else us_Date[0:2]
if len(MM) == 2:
    DD = us_Date[3] if us_Date[4] == '/' else us_Date[3:5]
else:
    DD = us_Date[2] if us_Date[3] == '/' else us_Date[2:4]
MM = '0' + MM if len(MM) == 1 else MM
DD = '0' + DD if len(DD) == 1 else DD
    
YYYY = us_Date[-4:]
#output
print('Here is the formatted date:', DD + '.' + MM + '.' + YYYY)

"""Name: Ben Gertz
    Course: CMPS 1500
    Lab Section: Tuesday 5:00- 6:15 PM
    Assignment: Lab 1 Part 2
    Date: 09/10/2017
 """
#input
us_Date = input('Please enter date in MM/DD/YYYY format: ')
#calculations
'''
Determines the placement of the /'s so that the interpreter knows where in the
strings to take the numbers.
'''
MM = us_Date[0] if us_Date[1] == '/'  else us_Date[0:2]
if len(MM) == 2:
    DD = us_Date[3] if us_Date[4] == '/' else us_Date[3:5]
else:
    DD = us_Date[2] if us_Date[3] == '/' else us_Date[2:4]
MM = '0' + MM if len(MM) == 1 else MM #If the user inputs single digit months and dates this adds a zero before the number
DD = '0' + DD if len(DD) == 1 else DD
YYYY = us_Date[-4:]
'''
This section has the list of months and converts the string value of the month the user entered to a integer so that it can be used
to call the corresponding month in the list.
'''
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
MM = int(MM)
MM = months[MM - 1]
#output
print('Here is the formatted date:', MM, DD + ',', YYYY)

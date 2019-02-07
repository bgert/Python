"""Name: Ben Gertz
    Course: CMPS 1500
    Lab Section: Tuesday 5:00- 6:15 PM
    Assignment: Lab 1 Part 0
    Date: 09/9/2017
 """


#input

seconds = int(input("Please enter the number of seconds:"))
#computation
minutes = 0
hours = 0
'''

This section checks the amount of seconds that the user has input. Through the if/else chain it is determined
whether the amount of seconds devides to include hours and or minutes and or seconds. If it is determined
that one of those conditions exists the variables rhours, rminutes, and rseconds are labeled true depending
on which ones exist. Further it uses division and remainders to determine the value of hours, minutes, and
seconds if they exist at all and assigns the value to variables hours, minutes, and seconds.

'''
if seconds >= 3600:
    hours = seconds // 3600
    rhours = True
    if seconds % 3600 >= 60:
        remainder_Seconds = seconds % 3600
        minutes = remainder_Seconds // 60
        rminutes = True 
        if remainder_Seconds % 60 != 0:
            seconds = remainder_Seconds % 60
            rseconds = True
        else:
            rseconds = False
    elif seconds % 3600 == 0:
        rminutes = False
        rseconds = False
    else:
        rminutes = False
        rseconds = True
        seconds = seconds % 3600
elif 3600 > seconds >= 60:
    minutes = seconds // 60
    rminutes = True
    rhours = False
    if seconds % 60 != 0:
        seconds = seconds % 60
        rseconds = True
    else:
        rseconds = False
else:
    rminutes = False
    rhours = False
    rseconds = True
'''

This section determines whether the words hour, minute, and second should be plural or no depending on
whether or not each variable is one.

'''
plural_second = 'seconds' if seconds != 1 else 'second'
plural_minute = 'minutes' if minutes != 1 else 'minute'
plural_hour = 'hours' if hours != 1 else 'hour'

#output
'''

This section prints a different combination of hours, minutes, and seconds depending on whether or not their
corresponding rvariable was True.

'''
if rhours and rminutes and rseconds:
    print(hours, plural_hour, minutes, plural_minute, seconds, plural_second)
elif rhours and rminutes and not rseconds:
    print(hours, plural_hour, minutes, plural_minute)
elif rhours and rseconds and not rminutes:
    print(hours, plural_hour, seconds, plural_second)
elif rminutes and rseconds and not rhours:
    print(minutes, plural_minute, seconds, plural_second)
elif rhours and not rminutes and not rseconds:
    print(hours, plural_hour)
elif rminutes and not rhours and not rseconds:
    print(minutes, plural_minute)
else:
    print(seconds, plural_second)

''' Name: Ben Gertz
    Course: CMPS 1500
    Lab Section: Tuesday 5-6.15 PM
    Assignment: Lab 7 Part 1
    Date: 11/6/2017
    This file has a recursive and an iterative function for finding the Nth fibonacci.
'''
import time
def F(n):
    if n < 2:
        return n
    else:
        return F(n - 1) + F(n - 2)

def f(n):
    x = 0
    y = 1
    z = 1
    for i in range(0, n):
        x = y
        y = z
        z = x + y
    return x

timef10s = time.time()
print(f(10))
timef10e = time.time()
print((timef10e - timef10s))

timeF10s = time.time()
print(F(10))
timeF10e = time.time()
print((timeF10e - timeF10s))

timef20s = time.time()
print(f(20))
timef20e = time.time()
print((timef20e - timef20s))

timeF20s = time.time()
print(F(20))
timeF20e = time.time()
print((timeF20e - timeF20s))

timef30s = time.time()
print(f(30))
timef30e = time.time()
print((timef30e - timef30s))

timeF30s = time.time()
print(F(30))
timeF30e = time.time()
print((timeF30e - timeF30s))

timef40s = time.time()
print(f(40))
timef40e = time.time()
print((timef40e - timef40s))

timef40s = time.time()
print(F(40))
timef40e = time.time()
print((timef40e - timef40s))



#!/usr/bin/python3
import random
number = random.randint(-10, 10)
# YOUR CODE HERE

if number == 0 :
    print(str(number) + " is zero")
elif number > 0:
    print(str(number) + " is positive")
else: 
    print(str(number) + " is negative")
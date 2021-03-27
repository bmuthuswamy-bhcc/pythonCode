# !/usr/bin/env python3 

# Chapter 7 - input() function pauses the program and waits for the user to
# enter some TEXT!
# If we *know* that input is going to be an INTEGER, then use int() for conversion
number1 = int(input("Enter a number: "))
number2 = int(input("Enter another number: "))

print(f"{number1} + {number2} = {number1 + number2}")
# !/usr/bin/env python3

# Exception handling
print("Give me two numbers and I will divide them.")
print("Enter q to quit")

while True:
	first_number = input("First number: ")
	if first_number == 'q':
		break
	second_number = input("Second number: ")
	if second_number == 'q':
		break

	try : 
		answer = int(first_number)/int(second_number)
	except ZeroDivisionError:
		print("You cannot divide by 0")
	except ValueError:
		print("Please enter an integer!")
	else: 
		print(answer)

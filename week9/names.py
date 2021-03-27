# !/usr/bin/env python3 

from name_function import get_formatted_name

print("Enter q at any time to quit.")
while True:
	first = input("Please enter a first name: ")
	if first == 'q':
		break

	if first.isdigit():
		print("Please enter a valid first name")
		continue # start next iteration of the loop

	last = input("Please enter a last name: ")
	if last == 'q':
		break

	if last.isdigit():
		print("Please enter a valid last name")
		continue

	formatted_name = get_formatted_name(first, last)
	print(f"Neatly formatted name: {formatted_name}.")
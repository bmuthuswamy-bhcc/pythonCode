# Write a program that for numbers 1 through 100,
# displays foo if the number is divisible by 5, 
# displays bar if the number is divisible by 3,
# displays foo_bar if the number is divisible by both
# displays the number itself if number is not divisible by 5 or 3

for number in range(1,101):
	if (number % 15) == 0:
		print('foo_bar')
	elif (number % 5) == 0:
		print('foo')
	elif (number % 3) == 0:
		print('bar')
	else:
		print(number)


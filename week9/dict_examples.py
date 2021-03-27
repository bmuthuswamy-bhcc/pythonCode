# !/usr/bin/env python3

import math # Import math library into current frame

# Dictionaries store KEY : VALUE pairs
alien_0 = {} # EMPTY dictionary
alien_0['x_position'] = 2 # Add some KEY-VALUE pairs
alien_0['y_position'] = 5
alien_0 ['color'] = 'green'
alien_0['points'] = 7
alien_0['speed'] = 'medium'
print(f"Original position: {alien_0['x_position']}")

# Move alien in the +ve (positive) x direction
if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else: # fast
	x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")

print(alien_0)
# remove a KEY : VALUE pair
del alien_0['points']
print(alien_0)

# Now, lets use the get method
points = alien_0.get('points', 'No point value assigned') # if point does not exist, get returns second argument
print(points)

# Iterating through dictionary - use items() method
#for key,value in alien_0.items():
# print(f"\nKey: {key}")
# print(f"Value: {value}")

# Another approach - keys()
#for key in alien_0.keys():
#print(key)
#for value in alien_0.values():
#print(value)

# List of dictionaries
alien_1 = {'x_position' : -3, 'y_position' : 12, 'color' : 'red', 'speed' : 'fast'}
aliens = [alien_0, alien_1]
# Print the color of each alien
for alien in aliens:
	print(alien['color'])

# alien_0[0] = 3014 # Integer keys are allowed - can be used to implement hash algorithms
# pi = 3.14
# alien_0[0] = math.pi 
# alien_0[1] = pi


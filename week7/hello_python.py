nameList = [] # Empty list initialization.  Useful for building lists from scratch
nameList.append("Carl")
nameList.append("Ferenc")
nameList.append("Bharath")
for name in nameList: # Lists are ITERATABLE in python!
	if name == "Ferenc":
		print(f'Hello {name.upper()}')
	elif name == "Carl":
		print(f'Hello {name.lower()}')
	else:
		print(f'Hello {name}')


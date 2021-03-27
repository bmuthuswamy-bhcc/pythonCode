def get_formatted_name(first, last,  middle=''): # default (or optional = '') arguments *MUST* be listed last
	"""Generate a nearly formatted full name."""
	if middle:
		full_name = f"{first} {middle} {last}"
	else:
		full_name = f"{first} {last}"
	return full_name.title()

# kwargs is a common parameter name to collect arbitrary 
# input arguments.
# Note that """...""" is called a DOC STRING (documentation string)
def build_profile(first, last, **kwargs): # ** builds a DICTIONARY of arbitrary kwargs, * builds tuples
	"""Build a dictionary containing everything we know about a person
	"""
	kwargs['first_name'] = first
	kwargs['last_name'] = last
	return kwargs

if __name__ == "__main__":
	user_info = build_profile('albert','einstein',location='princeton',field='physics')
	print(user_info['first_name'])
	print(user_info['last_name'])

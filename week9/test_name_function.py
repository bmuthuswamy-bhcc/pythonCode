# We should always test our code!
# Ideally we test if our FUNCTION (or CLASS) responds "correctly"
# to EVERY POSSIBLE input combination. Obviously, this is unrealistic
# Hence, we use ideas from Test Driven Development.  Nowadays, this approach
# is also called scrum (named after Rugby scrum). 
# Essentially we write a variety of TEST CASES to test our FUNCTIONs (CLASSEs).
# Each test case is called a UNIT TEST.  Hence, test driven development is also
# called unit testing.
import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
	def test_get_formatted_name(self):
		"""Do names like 'Bharath Muthuswamy' work?"""
		formatted_name = get_formatted_name('bharath', 'muthuswamy')
		self.assertEqual(formatted_name, 'Bharath Muthuswamy')


# Have an option of running this file directly *or* importing in another module
# __name__ is a special variable name which is set when the program is executed
# If this file is being run as the main program, __name__ is set to __main__
if __name__ == '__main__' :
	unittest.main()
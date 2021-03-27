class Dog:
	"""A simple object oriented approach to describing a dog"""
	def __init__(self, name, age):
		"""__init__ method is equivalent to a constructor.
		It is a special method that Python runs automatically whenever
		we create a new instance (object) of type Dog.
		self is a Python KEYWORD that refers to the current instance.
		It *must* be the first argument in a method.  So a method that
		takes no arguments still has self as the first argument (see sit
		method in this class)
		This is equivalent to this in C#
		"""
		self.name = name
		self.age = age

	def sit(self):
		"""Simulate a dog sitting in response to a command."""
		print(f"{self.name} is now sitting.")


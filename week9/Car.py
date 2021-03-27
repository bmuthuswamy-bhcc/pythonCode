class Car:
	"""A simple attempt to represent a car."""

	def __init__(self, make, model, year, odometer_reading_km=0):
		"""Initialize attributes to describe a car, with default values
		"""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading_km = odometer_reading_km # default value is 0

	def read_odometer(self):
		print(f"This car has {self.odometer_reading_km} kms on it.")

	def set_odometer_reading_km(self, odometer_reading_km):
		self.odometer_reading_km = odometer_reading_km

	def get_odometer_reading_km(self):
		return self.odometer_reading_km

	def fill_gas_tank(self):
		print("Please fill my gas tank!")

# Inheritance
class ElectricCar(Car):
	"""Represents aspects ofa  car, specific to electric vehicles."""
	def __init__(self,make,model,year, odometer_reading_km, battery_size):
		# Use super() method to call parent class methods!
		super().__init__(make,model,year,odometer_reading_km)
		self.battery_size = battery_size

	def fill_gas_tank(self):
		""" OVERRIDE parent method fill_gas_tank """
		print("Electric cars do not have a gas tank!")
		super().fill_gas_tank()


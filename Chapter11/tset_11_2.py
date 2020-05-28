
'''
import unittest
from pg291 import city_country_population

class City2TestCase(unittest.TestCase):
	"""Tests for 'name_function.py'."""

	def test_city_country_population(self):
		"""Do names like 'Janis Joplin' work?"""
		formatted_city_country_population = city_country_population('santiago', 'chile')
		self.assertEqual(formatted_city_country_population, 'Santiago, Chile')

if __name__ == '__main__':
	unittest.main()

'''

import unittest
from pg291 import name_country_pop

class CityTestCase(unittest.TestCase):
	"""Tests for 'name_function.py'."""

	def test_city_country(self):
		"""Do names like 'Janis Joplin' work?"""
		country = name_country_pop('santiago', 'chile')
		self.assertEqual(country, 'Santiago - Chile')

	def test_name_country_pop(self):
		"""Do names like 'Wolfgang Amadeus Mozart' work?"""
		country = name_country_pop(
		'santiago', 'chile', '5000000')
		self.assertEqual(country, 'Santiago - Chile - 5000000')

if __name__ == '__main__':
	unittest.main()
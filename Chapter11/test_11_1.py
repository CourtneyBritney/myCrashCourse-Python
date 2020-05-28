import unittest
from pg291 import city_country

class CityTestCase(unittest.TestCase):
	"""Tests for 'name_function.py'."""

	def test_city_country(self):
		"""Do names like 'Janis Joplin' work?"""
		formatted_city_country = city_country('santiago', 'chile')
		self.assertEqual(formatted_city_country, 'Santiago, Chile')

if __name__ == '__main__':
	unittest.main()
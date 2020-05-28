#11-1

def city_country(name, country):
	"""should return a string."""
	place = f"{name}, {country}"
	return place.title()

#place = city_country('santiago', 'chile')
#print(f"\"{place}\"")


#11-2


def city_country_population(name, country, population):
	"""should return a place."""
	place_pop = f"{name}, {country}, {population}"
	return place.title()

#place_pop = city_country('santiago', 'chile', 5000000)
#print(f"\"{place_pop}\"")


def name_country_pop(name, country, population=''):
	"""Generate a neatly formatted full name."""
	if population:
		country = f"{name} - {country} - {population}"
	else:
		country = f"{name} - {country}"
	return country.title()
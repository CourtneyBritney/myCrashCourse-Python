#8-12


def sandwich(*sandwiches):
	"""Summarize the pizza we are about to make."""
	print("\nMaking a sandwiches with the following:")
	for food in sandwiches:
		print(f"-{sandwich}")

		sandwich('tomatoes', 'lettuce', 'extra cheese')


#8-13

def build_profile(first, last, **user_info):
	"""Build a dictionary containing everything we know about a user."""
	user_info['first_name'] = first
	user_info['last_name'] = last
	return user_info

user_profile = build_profile('courtney', 'alexander',
							location='eldorado park',
							field='programming')
print(user_profile)
		

#8-14


def make_car(color, tow_package, **car_info):
	car_info['type']
	car_info['model']
	return car_info

car_profile = make_car('audi', 'rope',
				type= 'audi',
				model= '2016')
print(car_profile)
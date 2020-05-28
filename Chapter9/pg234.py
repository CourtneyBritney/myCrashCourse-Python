#9-4


class Restaurant:

	def __init__(cafe, restaurant_name, cuisine_type):
		#initialize attributes to a restaurant
		cafe.restaurant_name = restaurant_name
		cafe.cuisine_type = cuisine_type
		cafe.number_served = 0
		cafe.number_served += 1
		cafe.number_served
		cafe.number_served = int(cafe.number_served)
		

	def get_descriptive_restaurant(cafe):
		#return a neatly formatted descriptive restaurant.
		long_name = f"{cafe.restaurant_name} {cafe.cuisine_type}"
		return long_name.title()

	def number_served(cafe):
		#print a statement showing the number served.
		print(f"You are number served {cafe.number_served}")

my_restaurant = Restaurant('mug&bean', 'plain omelette')
print(my_restaurant.get_descriptive_restaurant())


#9-5


class User:
	#a class called user.

	def __init__(user, first_name, last_name):
		#initialize a first_name and last_name attributes.
		user.first_name = first_name
		user.last_name = last_name
		user.login_attempts = 1


	def greet_user(user):
		#a simple greeting to the user.
		print(f"Hello, {first_name.title()}")

	def describe_user(user):
		#description of the user.
		username = f"{user.first_name} {user.last_name}."
		return username.title()

	def login_attempts(user):
		#how many times a user attempts to log in.
		print(f"This user attempts to log in {user.login_attempts} every now and then.")

my_user = User('Courtney', 'Alexander')
print(my_user.describe_user())








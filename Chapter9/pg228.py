#9-1


class Restaurant:
	''''a simple attempt to model a restaurant'''
	def __init__(food, restaurant_name, cuisine_type):
		'''initialize restaurant name and cuisine type attributes'''
		food.restaurant_name = restaurant_name
		food.cuisine_type = cuisine_type

	def going(food):
		'''people going to specific place to eat a certain cuisine'''
		print(f"The people enjoy going to {restaurant_name}.")

	def eating(food):
		'''people enjoy eating a certain cuisine'''
		print(f"Myself and my friends enjoy the {cuisine_type}. It is filling and delightful.")



#9-2


my_restaurant = Restaurant('Little Italy', 'italian cuisine')

print(f"I love the {my_restaurant.restaurant_name} restaurant")
print(f"From all the food and cuisines I have tasted the {my_restaurant.cuisine_type} is the best by far.")



#9-3


class User:
	#a class called user.

	def __init__(user, first_name, last_name):
		#initialize a first_name and last_name attributes.
		user.first_name = first_name
		user.last_name = last_name

	def greet_user(user):
		#a simple greeting to the user.
		print(f"Hello, {first_name.title()}")

	def describe_user(user):
		#description of the user.
		username = f"{user.first_name} {user.last_name}."
		return username.title()


my_user = User('Courtney', 'Alexander')
print(my_user.describe_user())








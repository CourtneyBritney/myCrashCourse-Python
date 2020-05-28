#4-10

players = ['charles', 'martina', 'michael', 'florence', 'eli']

print("Here are the first three items on my team:")
for player in players[:3]:
	print(player.title())

players = ['charles', 'martina', 'michael', 'florence', 'eli']

print("Three items from the middle of the list are:")
for player in players[1:4]:
	print(player.title())


players = ['charles', 'martina', 'michael', 'florence', 'eli']

print("The last three items in the list are:")
for player in players[2:]:
	print(player.title())


#4-11

my_pizza = ['Chicken Tikka', 'Pepperoni', 'Margharita', 'Baconini']
friend_pizzas = my_pizza[:]

my_pizza.append('rib pizza')
friend_pizzas.append('huawian')

print("\nMy favorite pizza is:")
print(my_pizza)

print("\nMy My favorite pizza is:")
print(friend_pizzas)

for pizza in my_pizza:
	print(f"My favorite pizzas are {pizza.title()}")
	print(f"My friends favorite pizzas are {pizza.title()}.")	

#4-12

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)	

for food in my_foods[2:]:
	print(food.title())

for player in players[2:]:
	print(player.title())
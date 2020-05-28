#5-3

alien_colors = ['green', 'yellow', 'red']
if 'green' in alien_colors:
	print("You have earned 5 points")
if 'pink' in alien_colors:
	print("You have earned 5 points")

#5-4

alien_color = 'green'
if alien_color == 'green':
	print("You have earned 5 points for shooting the alien")
else: 
	print("You have earned 10 points")


#5-5
alienColour = 'purple'

if alienColour == 'green':
	print("You have earned 5 points")
elif alienColour == 'yellow':
	print("You have earned 10 points")
elif alienColour == 'red':
	print("You have earned 15 points")
else:
	print("Invalid colour!")


#5-6

age = 65 

if age < 2:
	print("Person is a baby")
elif age >= 2 and age < 4:
	print("Person is a toddler")
elif age >= 4 and age < 13:
	print("Person is a kid")
elif age >= 13 and age < 20:
	print("Person is a teeenager")
elif age >= 20 and age < 65:
	print("Person is an adult")
else:
	print("Person is an elder")


#5-7

favourite_fruit = ['Apple', 'Cherry', 'Watermelon']
if 'Apple' in favourite_fruit:
	print("I really like apples")
if 'Cherry' in favourite_fruit:
	print("I really like Cherry")
if 'Watermelon' in favourite_fruit:
	print("I really like Watermelon")
if 'peach' in favourite_fruit:
	print("I really like peach")
else:
	print("peach is not in the list!")

if 'plum' in favourite_fruit:
	print("I really like plum")
else:
	print("plum is not in the list!")
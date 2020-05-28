class Dog:
	'''creating a model called Dog'''

	def __init__(self, name, age):
		'''initializing attributes'''
		self.name = name
		self.age = age

	def sit(self):
		'''behavior'''
		print(f"{self.name} is now sitting.")

	def roll_over(self):
		'''behavior'''
		print(f"{self.name} rolled over!")

my_dog = Dog('Browny', 6)
your_dog =Dog('Willie', 5)

print(f"My dogs name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

print(f"Your dogs name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")



my_dog.sit()
my_dog.roll_over()
your_dog.sit()

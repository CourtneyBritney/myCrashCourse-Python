#10-3

filename = 'guest.txt'

prompt = input("What is your name?")

with open(filename, 'w') as file_object:
	file_object.write(f"{prompt.title()}")


#10-4

filename = 'guest_book.txt'
prompt = ("What is your name?")

new = True

while new:
	name = input(prompt)
	print(f"Hello, {name.title()}")
	repeat = input("Would you like to add a new name? (yes/ no) ")

	if repeat == 'no':
		new = False

	with open(filename, 'w') as file_object:
		file_object.write(f"{name.title()}\n")



#10-5


filename = 'responses.txt'
prompt = ("Why do you like programming?")

response = True

while response:
	response = input(prompt)
	print(f"Would you like to to add a new response? (yes/ no)")
	repeat = input("Would you like to add a new name? (yes/ no)")

	if repeat == 'no':
		response = False

	with open(filename, 'w') as file_object:
		file_object.write(f"{response.title()}\n")











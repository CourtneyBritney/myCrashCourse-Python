#10-6


prompt = ("Give me two numbers, and I'll add them.\n")
prompt += ("Enter 'q' to quit")

if input(prompt) == '':
	print("Value is not a number")
else:
	print(answer)


#10-7


prompt = ("Give me two numbers, and I'll add them.\n")
prompt += ("Enter 'q' to quit")

while True:
	first_number = input("\nFirst number:")
	if first_number == 'q':
		break 
	second_number = input("Second number:")
	if second_number == 'q':
		break
	answer = int(first_number) + int(second_number)
	print(answer)


#10-8


filename = 'cats.txt'

try:
	with open(filename) as f:
		contents = f.read()
except FileNotFoundError:
	print(f"Sorry, the file {filename} does not exist.")



#10-9


filename = 'cats.txt'

try:
	with open(filename) as f:
		contents = f.read()
except FileNotFoundError:
	print(f"Sorry, the file {filename} does not exist.")
	pass
else:
	print(filename)

	filenames = ['cats.txt']
	for file in filename:
		read(filename)
	










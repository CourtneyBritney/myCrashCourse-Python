with open ('pi_digits.txt') as file_object:
	contents = file_object.read()
	print(contents)

filename = 'pi_digits.txt'

with open ('pi_digits.txt') as file_object:
	for line in file_object:
		print(line)


filename = 'pi_digits.txt'

with open ('pi_digits.txt') as file_object:
	lines = file_object
	for line in lines:
		print(line.rstrip())




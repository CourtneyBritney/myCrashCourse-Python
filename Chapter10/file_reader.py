with open ('info.txt') as file_object:
	contents = file_object.read()
	print(contents)


filename = 'info.txt'

with open ('info.txt') as file_object:
	for line in file_object:
		print(line)


filename = 'info.txt'

with open ('info.txt') as file_object:
	for line in file_object:
		print(line.rstrip())


filename = 'info.txt'

with open ('info.txt') as file_object:
	lines = file_object.readlines()
	for line in lines:
		print(line.rstrip())

info = ''
for line in lines:
	info += line.rstrip()

print(info)
print(len(info))

prompt = input("What is your name and surname?")
prompt += (f"\nEnter 'q' to end the program")
full_name = f"{name} {surname}"

if name and surname:
	print(full_name)
else:
	print(input)
#6-4

glossary = {'arrays': 'means lists', 'booleans': 'is True or False', 'dictionaries': 'means objects', 'string': 'is quotation marks', 'integer': 'are whole numbers'}
glossary = {
'arrays': 'means lists',
'booleans': 'is True or False',
'dictionaries': 'means objects',
'string': 'is quotation marks',
'integer': 'are whole numbers',
}

for k, v in glossary.items():
	print(f"\nKey: {k}")
	print(f"Value: {v}")


#6-5


rivers = {'nile river': 'egypt', 'orange river': 'south africa', 'amazon river': 'south america'}

for river, country in rivers.items():
	print(f"The {river.title()} runs through {country.title()}.")


for river in rivers.keys():
	print(f"\n{river.title()}")

for country in rivers.values():
	print(f"\n{country.title()}")


#6-6


favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
'courtney': 'python'
}

for name in sorted(favorite_languages.keys()):
	print(f"{name.title()}, thank you for taking the poll.")
	print(f"{name.title()}, you are invited to take the poll.")


	








	
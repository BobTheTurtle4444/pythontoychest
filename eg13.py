# 13.py - This program illustrates the use of dictionaries, which is a name value pair.
cities = {
	'CA': 'San Francisco',
	'MI': 'Detroit',
	'FL': 'Jacksonville'
}
print(cities['CA'])
city = cities.get('MD')
if not city:
	print("Sorry, no Maryland.\n")
for k, v in cities.items():
	print(k, v)

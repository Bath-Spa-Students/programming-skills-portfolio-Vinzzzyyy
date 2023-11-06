rivers = {
    'nile': 'egypt',
    'amazon': 'south america',
    'yangtze': 'china',
}

for river, country in rivers.items():
    print("The " + river.title() + " flows through " + country.title() +".")

print("\nThe following rives are included in this data set:")
for river in rivers.keys():
    print("- " + river.title())

print("\nThe following countries are included in this data set:")
for country in rivers.values():
    print("- " + country.title())
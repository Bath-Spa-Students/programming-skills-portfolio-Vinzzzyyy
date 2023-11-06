pets = []

pet = {
    'animal type': 'Cat',
    'name': 'Shiro',
    'owner': 'Katheryn',
    'favorite food': 'Fish',
}
pets.append(pet)

pet = {
    'animal type': 'Dog',
    'name': 'Jack',
    'owner': 'Cole',
    'favorite food': 'Steak',
}
pets.append(pet)

pet = {
    'animal type': 'Python',
    'name': 'Zyra',
    'owner': 'Medusa',
    'favorite food': 'Rats',
}
pets.append(pet)

for pet in pets:
    print("\nThis is what i know about " + pet['name'].title() + ":")
    for key, value in pet.items():
        print("\t" + key + ": " + str(value))
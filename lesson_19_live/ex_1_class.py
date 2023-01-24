from datetime import datetime


class Animal:
    family_name = 'K9s'

    def __init__(self, name, species):
        self.name = name
        self.date_of_birth = datetime.now()
        self.species = species
        self.partner = None


print(Animal.family_name)

normal = Animal('Barsik', 'Dog')
print(normal.name)
print(normal.family_name)
print()
Animal.family_name = 'Something else'
print(normal.family_name)

new_animal = Animal('Kuzea', 'Dog')
print(new_animal.name)
print(new_animal.family_name)
print(new_animal.date_of_birth)
print(new_animal.species)
print(new_animal.partner)

new_animal.partner = Animal('Wiskies', 'Cat')
print(new_animal.partner.family_name)

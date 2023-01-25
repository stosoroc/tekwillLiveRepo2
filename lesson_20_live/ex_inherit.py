from datetime import datetime


class Animal:

    def __init__(self, name, species, date_of_birth):
        self.species = species
        self.name = name
        self.date_of_birth = date_of_birth

    def __str__(self):
        return f'{self.species} {self.name}'

    def eat(self):
        return f'{str(self)} is eating'

    def eat_3_times(self):
        for a in range(3):
            print(self.eat())


class Dog(Animal):

    def __init__(self, breed, *args, **kwargs):
        kwargs['species'] = 'Dog'
        super().__init__(*args, **kwargs)
        self.breed = breed

    def __str__(self):
        return f'Dog {self.breed} {self.name}'

    def bark(self):
        print('Woof')


patrik = Animal('Patrik', species='Star', date_of_birth=datetime.now())
kuzea = Dog(breed='Dvorneaga', name='Kuzea', date_of_birth=datetime.now())
patrik.eat_3_times()
kuzea.eat_3_times()
kuzea.bark()

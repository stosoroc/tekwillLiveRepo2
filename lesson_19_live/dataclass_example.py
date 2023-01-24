from dataclasses import dataclass
from datetime import datetime


@dataclass
class Animal:
    name: str
    species: str
    date_of_birth: datetime

    def say_hi(self):
        print(f'{self.species} {self.name} says HI')


kuzea = Animal('Kuzea', 'Dog', datetime.now())
print(kuzea)
kuzea.say_hi()
print(type(Animal))
print(Animal.say_hi.__name__)
print(Animal.__name__)

from datetime import datetime


class Pet:
    pet_name: str
    pet_type: str
    pet_food: str
    
    def __init__(self, pet_name, pet_type, pet_food):
        self.pet_name = pet_name
        self.pet_type = pet_type
        self.pet_food = pet_food 
    
    def get_name_food(self):
        return (f'{self.pet_type} called {self.pet_name} that loves {self.pet_food}')

class HumanWithPet:
    first_name: str
    last_name: str
    date_of_birth: datetime.date
    pets: dict
    
    
    def __init__(self, first_name, last_name, date_of_birth):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = datetime.strptime(date_of_birth, '%d/%m/%Y')
        self.pets = []        
    
        
    def adopt_new_pet(self, pet):
        self.pets.append(pet)
    
    def give_away_pet(self, pet):
        self.pets.remove(pet)
        
    def __str__(self):
        if len(self.pets) == 0:
            return (f'{self.first_name} {self.last_name} age {datetime.today().year - self.date_of_birth.year}')  + " with no pets"
        elif len(self.pets) == 1:
            return (f'{self.first_name} {self.last_name} age {datetime.today().year - self.date_of_birth.year}') + " with a pet: " + str(self.pets[0].get_name_food())
        else:
            return (f'{self.first_name} {self.last_name} age {datetime.today().year - self.date_of_birth.year}') + " with " + str(len(self.pets)) + " pets: " + ", ".join(str(pet.get_name_food()) for pet in self.pets)
        
user = HumanWithPet('Ion','Marescu','01/02/2000')

pet_cat = Pet('Garfield','Cat','lasagna')
pet_dog = Pet('Cooper','Dog','bones')
pet_bird = Pet('Zippy','Bird','zucchini')

#print(user.get_full_name(),user.get_age(),user.get_name_food())

print(user)

user.adopt_new_pet(pet_cat)
print(user)

user.adopt_new_pet(pet_dog)
user.adopt_new_pet(pet_bird)
print(user)

user.give_away_pet(pet_cat)
print(user)




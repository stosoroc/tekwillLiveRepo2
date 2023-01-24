from datetime import datetime

class HumanWithPet:
    first_name: str
    last_name: str
    date_of_birth: datetime.date
    pet_name: str
    pet_type: str
    pet_food: str
    
    def __init__(self, first_name, last_name, date_of_birth, pet_name, pet_type, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = datetime.strptime(date_of_birth, '%d/%m/%Y')
        self.pet_name = pet_name
        self.pet_type = pet_type
        self.pet_food = pet_food        
    
    def get_full_name(self):
        return (f'{self.first_name} {self.last_name}')
    
    def get_age(self):
        return (f'age {datetime.today().year - self.date_of_birth.year} with a pet:')
    
    def get_name_food(self):
        return (f'{self.pet_type} called {self.pet_name} that loves {self.pet_food}')
    
user = HumanWithPet('Ion','Marescu','01/02/2000','Cooper','Dog','bones')
print(user.get_full_name(),user.get_age(),user.get_name_food())
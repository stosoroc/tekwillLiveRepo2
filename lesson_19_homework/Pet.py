class Pet:
    name: str
    pet_type: str
    fav_food: str
    
    def __init__(self, name, pet_type, fav_food):
        self.name = name
        self.pet_type = pet_type
        self.fav_food = fav_food
    
    def get_name_food(self):
        return (f'{self.pet_type} called {self.name} that loves {self.fav_food}')
    
    
    
if __name__ == '__main__':            
    pet_cat = Pet('Garfield','Cat','lasagna')
    pet_dog = Pet('Cooper','Dog','bones')
    pet_bird = Pet('Zippy','Bird','zucchini')

    print(pet_cat.get_name_food())
    print(pet_dog.get_name_food())
    print(pet_bird.get_name_food())
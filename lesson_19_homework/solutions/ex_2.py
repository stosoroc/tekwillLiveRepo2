from datetime import datetime, date

from lesson_19_homework.solutions.ex_1 import Human


class Pet:

    def __init__(self, name, type, fav_food):
        self.name = name
        self.type = type
        self.fav_food = fav_food

    def __str__(self):
        return repr(self)

    def __repr__(self):
        return f"{self.type.capitalize()} called {self.name.capitalize()} that loves {self.fav_food}"


class HumanWithPet(Human):

    def __init__(self, first_name: str, last_name: str, date_of_birth: date, list_of_pets=None):
        super().__init__(first_name, last_name, date_of_birth)
        self.list_of_pets = list_of_pets or []

    def add_new_pet(self, pet_to_adopt):
        self.list_of_pets.append(pet_to_adopt)

    def give_away_pet(self, pet_to_remove):
        self.list_of_pets.remove(pet_to_remove)

    def __repr__(self):
        if len(self.list_of_pets) == 0:
            return f"{super().__str__()} with no pets"
        if len(self.list_of_pets) == 1:
            return f"{super().__str__()} with a pet: {str(self.list_of_pets[0])}"
        return f"{super().__str__()} with {len(self.list_of_pets)} pet:" \
               f" {','.join([str(pet) for pet in self.list_of_pets])}"

    def __str__(self):
        return repr(self)


def test_pet():
    dog = Pet('Barsik', 'dog', 'meat')
    cat = Pet('Puffie', 'cat', 'lasagna')
    print(dog)
    print(cat)


def test_human_with_pet():
    dog = Pet('Barsik', 'dog', 'meat')
    cat = Pet('Puffie', 'cat', 'lasagna')
    marius = HumanWithPet('Marius', 'Tricolici', date(2000, 10, 12), [dog, cat])
    print(marius.list_of_pets)
    print(marius.list_of_pets[0].name)
    print(marius)
    marius.give_away_pet(dog)
    print(marius)
    marius.give_away_pet(cat)
    print(marius)


if __name__ == '__main__':
    test_pet()
    test_human_with_pet()

class Animal:

    def __init__(self, name, species):
        self.name = name
        self.species = species


class AnimalThatSleeps(Animal):

    def __init__(self, sleep_time):
        self.sleep_time = sleep_time

    def sleep(self):
        pass


class AnimalThatEats(Animal):

    def __init__(self, food):
        self.food = food

    def eat(self):
        pass


class Dog(AnimalThatSleeps):

    def __init__(self, name):
        self.name = name
        self.species = 'Dog'

    def bark(self):
        pass


class AnimalThatEatsAndSleeps(AnimalThatEats, AnimalThatSleeps):

    def __init__(self, name, food, sleep_time):
        AnimalThatEats.__init__(self, food)
        AnimalThatSleeps.__init__(self, sleep_time)
        Animal.__init__(self, name, 'Dog')

    def print_info(self):
        print(self.food, self.sleep_time, self.name)


print(AnimalThatEatsAndSleeps.mro())
AnimalThatEatsAndSleeps('Kuzea', 'Lasagna', 10).print_info()

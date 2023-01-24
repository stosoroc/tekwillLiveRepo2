class Animal:

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def say_hi(self):
        print(f'{self.species} {self.name} says HI!')

    def say_hi_n_times(self, times=1):
        for time in range(times):
            print(f'{self.species} {self.name} says HI!')


kuzea = Animal('Kuzea', 'Dog')
kuzea.say_hi()

barsik = Animal('Barsik', 'Dog')
barsik.say_hi()

kuzea.say_hi_n_times(2)
barsik.say_hi_n_times(times=4)
kuzea.say_hi_n_times()

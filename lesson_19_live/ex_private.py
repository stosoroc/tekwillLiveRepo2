from datetime import datetime


class Animal:

    def __init__(self, name, species):
        self._name = name
        self._species = species

    def __str__(self):
        return f"Animal {self._species} named {self._name}"

    def say_hi(self):
        print(f'{self._species} {self._name} says HI!')

    def get_name(self):
        return self._name

    def _validate_new_name(self, new_name):
        if not isinstance(new_name, str):
            raise Exception('Name must be string')

    def set_name(self, name):
        self._validate_new_name(name)
        self._name = name

    def set_species(self, new_value, god_mode=False):
        if not god_mode:
            raise Exception('Not allowed to change species')
        self._species = new_value

    def get_species(self):
        return self._species

    def say_hi_n_times(self, times=1):
        for time in range(times):
            self.say_hi()


print(datetime.now())
kuzea = Animal('Kuzea', 'Dog')
print(kuzea)
kuzea_str = str(kuzea)
print(kuzea_str)


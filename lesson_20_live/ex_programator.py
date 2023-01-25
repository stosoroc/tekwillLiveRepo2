class Person:

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        if self._name == None:
            return 'Anonymous'
        return self._name

    @name.setter
    def name(self, new_val):
        if new_val is None:
            raise Exception("Cant set new name to none")
        self._name = new_val


class Angajat(Person):

    def __init__(self, pozitie, salariu, name, age):
        super().__init__(name, age)
        self.pozitie = pozitie
        self.salariu = salariu


class Programator(Angajat):

    def __init__(self, limbaje_de_programare, pozitie, salariu, name, age):
        super().__init__(pozitie, salariu, name, age)
        self.limbaje_de_programare = limbaje_de_programare


programator = Programator(["Python"], 'Developer', 12031, 'Marius', 112)
print(programator.name)
programator.name = 'Andrei'
print(programator.name)

agj = Angajat('Developer', 12031, None, 112)
print(agj.name)
agj.name = None

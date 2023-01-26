class Animal:

    def _age(self):
        pass

    def print_age(self):
        print(self._age())


class Dog(Animal):

    def _age(self):
        pass

    def access_age(self):
        return self._age()

class Example:

    def __init__(self):
        self.a = 10

    def execute(self, a, b):
        print(a, b)

    @property
    def age(self):
        return 'Something'


ex = Example()
print(ex)

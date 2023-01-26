from datetime import datetime, date


class Human:

    def __init__(self, first_name: str, last_name: str, date_of_birth: date):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_age(self):
        today = datetime.now().date()
        # 2023 - 2000 = 23
        not_passed = (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day)
        number_of_years = today.year - self.date_of_birth.year - int(not_passed)
        return number_of_years

    def __str__(self):
        return f"{self.get_full_name()}, age {self.get_age()}"


def test_human():
    marius = Human('Marius', 'Tricolici', datetime(2000, 10, 12))
    marius_string = str(marius)
    print(marius_string)
    print(marius)
    print(marius.get_full_name())
    print(marius.get_age())


if __name__ == '__main__':
    test_human()

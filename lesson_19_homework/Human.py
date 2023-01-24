from datetime import datetime

class Human:
    first_name: str
    last_name: str
    date_of_birth: datetime.date
    
    def __init__(self, first_name, last_name, date_of_birth):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = datetime.strptime(date_of_birth, '%d/%m/%Y')
    
    def get_full_name(self):
        return (f'{self.first_name} {self.last_name}')
    
    def get_age(self):
        return (f'age {datetime.today().year - self.date_of_birth.year}')
    
    
user = Human('Ion','Marescu','01/02/2000')
print(user.get_full_name(),user.get_age())
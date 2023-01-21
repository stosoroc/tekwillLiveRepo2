from datetime import datetime


def calculate_days_until_birthday(birth_date: datetime):
    birthday_this_year = datetime(
        datetime.now().year,
        birth_date.month,
        birth_date.day
    )
    already_passed = birthday_this_year < datetime.now()
    cp_to = birthday_this_year
    if already_passed:
        cp_to = datetime(
            datetime.now().year + 1,
            birth_date.month,
            birth_date.day
        )
    delta = cp_to - datetime.now()
    return delta.days + 1


def register_customer():
    fn = input('FN:')
    ln = input('LN:')
    dob = input('DOB (DD/MM/YY):')
    dob = datetime.strptime(dob, '%d/%m/%Y')
    print(
        f"Customer {fn}, {ln} has birthday in {calculate_days_until_birthday(dob)}"
    )


register_customer()

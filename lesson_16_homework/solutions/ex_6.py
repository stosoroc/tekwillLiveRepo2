import json
from datetime import datetime


def list_all_employees(emp_list: list):
    for emp in emp_list:
        print(emp['name'])


def list_all_position(emp_list: list):
    positions = set()
    for emp in emp_list:
        positions.add(emp['position'])
    for position in positions:
        print(position)


def calculate_to_pay_monthly(emp_list: list):
    to_pay = sum([emp['salary'] for emp in emp_list])
    print(f'To pay {to_pay}')
    return to_pay


def calculate_tax_montly(emp_list: list):
    tax_percent = input('Procente Taxe (%): ')  # 20
    tax_percent = float(tax_percent) / 100
    print(f'{calculate_to_pay_monthly(emp_list) * tax_percent:0.02f}')


def get_salary(employee):
    return employee['salary']


def show_to_10_highest_paid(emp_list: list):
    emp_list.sort(key=get_salary, reverse=True)
    print('Highest paid employees')
    for employee in emp_list[0:10]:
        print(
            f"{employee['name']} working as {employee['position']} since "
            f"{employee['employee_from']} with salary {employee['salary']}"
        )


def show_to_10_oldest_employees(emp_list: list):
    print('\n Longest working employees')
    DATE_FORMAT = '%m/%d/%Y'
    for employee in emp_list:
        employee['employee_from'] = datetime.strptime(employee['employee_from'], DATE_FORMAT)
    emp_list.sort(key=lambda a: a['employee_from'])
    for employee in emp_list[0:10]:
        print(
            f"{employee['name']} working as {employee['position']} since "
            f"{employee['employee_from']} with salary {employee['salary']}"
        )


def get_emp_list():
    "\n, \t, \\"
    with open(
            'C:\\Users\\mariu\\PycharmProjects\\tekwillLiveRepo2\\lesson_16_homework\\files\\employee_list.json'
    ) as file:
        return json.load(file)


if __name__ == '__main__':
    emp_list = get_emp_list()
    list_all_employees(emp_list)
    list_all_position(emp_list)
    calculate_to_pay_monthly(emp_list)
    calculate_tax_montly(emp_list)
    show_to_10_highest_paid(emp_list)
    show_to_10_oldest_employees(emp_list)

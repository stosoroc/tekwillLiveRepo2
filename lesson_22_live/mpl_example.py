import pandas as pd
import matplotlib.pyplot as plt

employees = pd.read_json(
    'C:\\Users\\mariu\\PycharmProjects\\tekwillLiveRepo2\\lesson_16_homework\\files\\employee_list.json')
average_by_position = employees.groupby('position').mean()

employees_with_more_than_200 = employees[employees['salary'] > 2500]

print(employees_with_more_than_200)

print(average_by_position)
average_by_position.plot(kind='pie', subplots=True)
plt.savefig('example.png')

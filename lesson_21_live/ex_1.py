# echivalent cu pd = pandas
import json

import pandas as pd

data = json.load(
    open("C:\\Users\\mariu\\PycharmProjects\\tekwillLiveRepo2\\lesson_16_homework\\files\\employee_list.json")
)
df = pd.DataFrame(data)
print(df)
print(df['salary'])
df.to_excel('example.xlsx')
df = pd.read_excel('example.xlsx')
print(df)

import pandas as pd

conv_28_ian = pd.read_json(
    'C:\\Users\\mariu\\PycharmProjects\\tekwillLiveRepo2\\lesson_21_homework\\conversion_rates.json')
conv_today = pd.read_json('http://www.floatrates.com/daily/mdl.json')
conv_28_ian = conv_28_ian.transpose()
conv_today = conv_today.transpose()
print(conv_today)

converion_diff = conv_today['inverseRate'] - conv_28_ian['inverseRate']

print(converion_diff)

sorted = converion_diff.sort_values()

difference_from = conv_28_ian['date']
difference_to = conv_today['date']

conv_today['diff'] = converion_diff
conv_today['from'] = difference_from
conv_today['to'] = difference_to

print(sorted)

print(conv_today)

#
# df_excell = pd.read_excel('C:\\Users\\mariu\\PycharmProjects\\tekwillLiveRepo2\\lesson_22_homework\\homework.xlsx')
# print(df_excell)

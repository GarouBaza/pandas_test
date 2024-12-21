import pandas as pd

a = {
    'Name': ['Maga', 'isa', 'ahmad', 'Musa'],
    'Age': [18, 33, 22, 16],
    'Country': ['USA', 'Mexico', 'Russia', 'UK']
}

df = pd.DataFrame(a)

'''Добавляем новый столбик'''
df['Zarplata'] = [122, 22, 44, 13]


'''Выдает рандом'''
# print(df.sample())

'''Сортирует по возрасту'''
# sorted_df = df.sort_values(by='Age')
# print(sorted_df)

'''Показывает от 16 лет'''
filtered_df = df[df['Age'] > 16]
print(filtered_df)

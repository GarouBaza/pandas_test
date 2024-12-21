import pandas
import pandas as pd

data = {
    'Employes': [101, 102, 103, 104, 105],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Department': ['HR', 'Finance', 'IT', 'Marketing', 'IT'],
    'salary': [70000, 80000, 75000, 60000, 72000],
    'JoiningDate': ['2020-01-15', '2019-03-12', '2021-07-23', '2018-11-30', '2019-05-19']
}

df = pd.DataFrame(data)

'''Первые 2'''
# print(df.head(2))
#

'''Последние 2'''
# print(df.tail(2))

'''Больше 70000'''
# filtered_df = df[df['salary'] > 70000]
# print(filtered_df)

'''Работают в IT'''
# filtered_df = df[df['Department'] == 'IT']
# print(filtered_df)

'''Среднаяя зп'''
# salary = df['salary'].mean()
# print(salary)

'''Макс'''
# salary2 = df['salary'].max()
# print(salary2)


'''В порядке убывание'''
# sorted_df = df.sort_values('salary', ascending=False)
# print(sorted_df)


'''Добавление нового столбца'''
# df['YearsAtCompany'] = [10, 2, 5, 3, 9]
# print(df)


'''Измениние'''
# df.loc[3, 'salary'] = 20
# print(df)
import pandas as pd

data = {
    'OrderID': [201, 202, 203, 204, 205],
    'Porduct': ['Laptop', 'Mouse', 'Keybord', 'Monitor', 'Mouse'],
    'Quantity': [1, 3, 2, 1, 2],
    'Price': [1200, 25, 75, 300, 25],
    'OrderDate': ['2024-01-10', '2024-01-11', '2024-01-12', '2024-01-13', '2024-01-14']
}

df = pd.DataFrame(data)

df['Total'] = df['Quantity'] * df['Price']
d = df['Total'].sum()

max_sales = df.groupby('Porduct')['Quantity'].max().reset_index()
print(max_sales)








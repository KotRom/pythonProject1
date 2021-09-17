import pandas as pd

df = pd.read_csv('csv_files/2019.csv')

# # iterrows() method will create an iterable object from rows
# for index, row in df.iterrows():
#     print(index, row)
#     print(row['Country or region'])
#

# Print row with condition
print(df.loc[df['Country or region'] == 'Estonia'])

# Description of dataframe
print(df.describe())

# Sorting by column
print(df.sort_values('Country or region', ascending=True))
print(df.sort_values(['GDP per capita', 'Generosity'], ascending=False))
print(df.sort_values(['Country or region', 'Generosity'], ascending=[1, 0]))

# Sum columns to a new one
df['Total'] = df['GDP per capita'] + df['Generosity'] + df['Perceptions of corruption']
print(df['Total'])

# Delete column from dataframe
df = df.drop(columns=['Total'])
print(df)

print(df.dtypes)

# Contains
print(df.loc[df['Country or region'].str.contains('on | an')])

# Conditions can be checked inside method
print(df.loc[df['GDP per capita'] < 1, ['Country or region']])

# Will group all cells with same value and mean() will return mean value of other cells
print(df.groupby('GDP per capita').mean().sort_values('Score', ascending=False))

# Sums all values and groups cells by given table
print(df.groupby('GDP per capita').sum())

# Counts how many times value is in table
print(df.groupby('GDP per capita').count())
print(df.groupby('GDP per capita').count()['Score'])

# Working with large data
for df in pd.read_csv('csv_files/2019.csv', chunksize=5):
    print('Chunk')
    print(df)


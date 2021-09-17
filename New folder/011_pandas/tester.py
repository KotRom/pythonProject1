import pandas as pd
import re

df = pd.read_csv('csv_files/2019.csv')

pd.set_option('display.max_columns', 9)
pd.set_option('display.max_rows', 160)
# # print(df)
# print(df.sort_values(['Country or region', 'Score'], ascending=[0, 1]))

print(df.loc[df['GDP per capita'] > 1, ['Country or region']])
#
# # pattern = re.compile('[A-Za-z]+[ -][A-Za-z]+')
# print(df.loc[df['Country or region'].str.contains(pattern), ['Country or region']])
#
# # print(df.groupby('Country or region').sum())
# #
# # print(df.groupby('Country or region').mean()['Score'])
# # print(df.groupby('Country or region').count()['Score'])
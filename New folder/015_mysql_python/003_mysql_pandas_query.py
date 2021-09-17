import mysql.connector
import pandas as pd

conn = mysql.connector.connect(
    user='root',
    password='12345678',
    host='localhost',
    database='sakila'
)

pd.set_option('display.max_columns', 10)  # Will set option on how many columns to show
pd.set_option('display.max_rows', 156)  # WIll set option on hpw many rows to show

# # Selects all tables in database
# sakila_data = pd.read_sql_query('SHOW TABLES FROM sakila', conn)
# print(sakila_data)
#
# # Select all data in happiness2 table
# df = pd.read_sql_query('SELECT * FROM film', conn)
# print(df)

# Creating dataframe with cursor
query = 'select film.title, actor.first_name, actor.last_name from film, actor ' \
        'order by actor.first_name, actor.last_name'
cursor = conn.cursor()
cursor.execute(query)
df = pd.DataFrame(cursor)
for x in df.groupby([df[1], df[2]]):
    print(x)

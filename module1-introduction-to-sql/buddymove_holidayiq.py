import os
import pandas as pd
import sqlite3

df = pd.read_csv('buddymove_holidayiq.csv').rename(columns={'User Id':'User_Id'})

DB_FILEPATH = os.path.join(os.path.dirname(__file__), "buddymove_holidayiq.sqlite3")

connection = sqlite3.connect(DB_FILEPATH)
print("CONNECTION:", connection)

df.to_sql('review', connection, if_exists='replace')

cursor = connection.cursor()
print("CURSOR", cursor)

num_rows = cursor.execute('select count(*) from review').fetchone()[0]
print(f'{num_rows=}')


num_users_nature_100_shopping_100 = cursor.execute('SELECT count(User_Id) from review WHERE Nature >= 100 and Shopping >= 100').fetchone()[0]
print(f'{num_users_nature_100_shopping_100=}')
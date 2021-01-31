import os
import psycopg2
import json
import pandas as pd




connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
print("CONNECTION", type(connection))

cursor = connection.cursor()
print("CURSOR", type(cursor))

print("-------------------")
query = "SELECT usename, usecreatedb, usesuper, passwd FROM pg_user;"
print("SQL:", query)
cursor.execute(query)
for row in cursor.fetchall()[0:10]:
    print(row)


df = pd.read_csv('titanic.csv')

print(df.columns)

cols = {'Survived':'survived', 'Pclass':'pclass', 'Name':'name', 'Sex':'sex', 'Age':'age', 'Siblings/Spouses Aboard':'si_sp_aboard',
       'Parents/Children Aboard':'pa_ch_aboard', 'Fare':'fare'}

df.rename(columns=cols, inplace=True)

print(df.columns)
#
# CREATE THE TABLE
#

table_name = "titanic"

print("-------------------")
query = f"""
-- CREATE TYPE gender AS ENUM ('male', 'female');
CREATE TABLE IF NOT EXISTS {table_name} (
  id SERIAL PRIMARY KEY,
  survived BOOLEAN NOT NULL,
  pclass SMALLINT NOT NULL,
  name varchar(40) NOT NULL,
  sex gender NOT NULL,
  age SMALLINT NOT NULL,
  si_sp_aboard BOOLEAN NOT NULL,
  pa_ch_abouard BOOLEAN NOT NULL,
  fare REAL NOT NULL
);
"""
print("SQL:", query)
cursor.execute(query)

connection.commit()



cursor.close()
connection.close()

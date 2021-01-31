import os
import psycopg2
from psycopg2 import extras
import json
import pandas as pd


def execute_values(conn, df, table):
    """
    Using psycopg2.extras.execute_values() to insert the dataframe
    """
    # Create a list of tupples from the dataframe values
    tuples = [tuple(x) for x in df.to_numpy()]
    # Comma-separated dataframe columns
    cols = ','.join(list(df.columns))
    # SQL quert to execute
    query  = f"INSERT INTO {table}({cols}) VALUES %s"
    cursor = conn.cursor()
    try:
        extras.execute_values(cursor, query, tuples)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        conn.rollback()
        cursor.close()
        return 1
    print("execute_values() done")
    cursor.close()



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

df = df.astype({'survived':'bool', 'si_sp_aboard':'bool', 'pa_ch_aboard':'bool'})
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
  name varchar NOT NULL,
  sex gender NOT NULL,
  age SMALLINT NOT NULL,
  si_sp_aboard BOOLEAN NOT NULL,
  pa_ch_aboard BOOLEAN NOT NULL,
  fare REAL NOT NULL
);
"""
print("SQL:", query)
cursor.execute(query)
connection.commit()

execute_values(connection, df, table_name)

cursor.close()
connection.close()

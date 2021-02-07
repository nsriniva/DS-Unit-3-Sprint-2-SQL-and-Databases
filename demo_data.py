import os
import sqlite3

demo_records = [
    ('g', 3, 9),
    ('v', 5, 7),
    ('f', 8, 7)
]

DB_FILEPATH = os.path.join(os.path.dirname(__file__), 'demo_data.sqlite3')

conn = sqlite3.connect(DB_FILEPATH)
print("CONNECTION:", conn)

c = conn.cursor()

# Create table
c.execute('''CREATE TABLE demo
             (s text, x integer, y integer)''')

#insert multiple records in a single query
c.executemany('INSERT INTO demo VALUES(?,?,?);',demo_records)

# Save (commit) the changes
conn.commit()

row_count = c.execute('select count(*) from demo').fetchone()[0]

print(f'{row_count = }')

xy_at_least_5 = c.execute('select count(*) from demo where x>=5 and y >=5').fetchone()[0]

print(f'{xy_at_least_5 = }')

unique_y = c.execute('select count(distinct y) from demo').fetchone()[0]

print(f'{unique_y = }')

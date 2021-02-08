import os
import sqlite3


DB_FILEPATH = os.path.join(os.path.dirname(__file__), 'demo_data.sqlite3')

conn = sqlite3.connect(DB_FILEPATH)

c = conn.cursor()

row_count = c.execute('select count(*) from demo').fetchall()

xy_at_least_5 = c.execute(
    'select count(*) from demo where x>=5 and y >=5').fetchall()

unique_y = c.execute('select count(distinct y) from demo').fetchall()

'''
row_count = 3
xy_at_least_5 = 2
unique_y = 2
'''

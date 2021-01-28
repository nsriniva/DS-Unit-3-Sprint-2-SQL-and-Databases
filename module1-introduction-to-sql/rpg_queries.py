import os
import sqlite3
from queries import *

# construct a path to wherever your database exists
#DB_FILEPATH = "chinook.db"
DB_FILEPATH = os.path.join(os.path.dirname(__file__), "rpg_db.sqlite3")

connection = sqlite3.connect(DB_FILEPATH)
print("CONNECTION:", connection)

cursor = connection.cursor()
print("CURSOR", cursor)


result = cursor.execute(TOTAL_CHARACTERS).fetchone()[0]
print("TOTAL_CHARACTERS:", result)

# necromancer is a subclass of mage
subclasses = ('cleric', 'fighter', 'mage', 'necromancer', 'thief')

for subclass in subclasses:
    result = cursor.execute(f'{TOTAL_SUBCLASS}{subclass}').fetchone()[0]
    print(f'TOTAL_SUBCLASS({subclass}):{result}')
    if subclass == 'necromancer':
        print('Necromancers are Mages!')

result = cursor.execute(TOTAL_ITEMS).fetchone()[0]
print("TOTAL_ITEMS:", result)

result = cursor.execute(WEAPONS).fetchone()[0]
print("WEAPNONS:", result)

result = cursor.execute(NON_WEAPONS).fetchone()[0]
print("NON_WEAPONS:", result)

result = cursor.execute(AVG_CHARACTER_ITEMS).fetchone()[0]
print("AVG_CHARACTER_ITEMS:", result)

result = cursor.execute(AVG_CHARACTER_WEAPONS).fetchone()[0]
print("AVG_CHARACTER_WEAPONS:", result)

result = cursor.execute(CHARACTER_ITEMS+' limit 20').fetchall()
print("CHARACTER_ITEMS:", result)

result = cursor.execute(CHARACTER_WEAPONS+' limit 20').fetchall()
print("CHARACTER_WEAPONS:", result)
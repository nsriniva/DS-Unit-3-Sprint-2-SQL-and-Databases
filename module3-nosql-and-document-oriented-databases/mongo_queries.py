# Working with MongoDB is easier than PostgreSQL - everything from creating a database to a table/collection(no schema needs to be specified) to bulk inserting rows/documents is way easier with MongoDB

from math import isnan
import pymongo
from dotenv import load_dotenv
from os import getenv, path
import sqlite3
import pandas as pd
from numpy import NaN,nan

load_dotenv()

CHARACTER_ITEMS_LIST = 'SELECT character_id, count(armory_item.name)  as num_items, group_concat(armory_item.name)  as items FROM charactercreator_character_inventory JOIN armory_item on charactercreator_character_inventory.item_id = armory_item.item_id GROUP BY character_id'

CHARACTER_WEAPONS_LIST = 'SELECT character_id, count(armory_item.name)  as num_weapons, group_concat(armory_item.name)  as weapons FROM charactercreator_character_inventory JOIN armory_item on charactercreator_character_inventory.item_id = armory_item.item_id WHERE charactercreator_character_inventory.item_id in (select item_ptr_id from armory_weapon) GROUP BY character_id'

DB_FILEPATH = path.join(path.dirname(__file__), '../module1-introduction-to-sql',"rpg_db.sqlite3")

connection = sqlite3.connect(DB_FILEPATH)
print("CONNECTION:", connection)

rpg_tables = {'charactercreator_character':None, 'charactercreator_character_inventory':None, 'armory_item':None,'armory_weapon':None}

for rpg_table in rpg_tables:
    rpg_tables[rpg_table] = pd.read_sql(f'select * from {rpg_table}', connection)
    #print(rpg_tables[rpg_table].to_dict('records'))

char_items_list = pd.read_sql(CHARACTER_ITEMS_LIST, connection)
char_items_list['items'] = char_items_list['items'].apply(lambda x: x.split(','))

char_weapons_list = pd.read_sql(CHARACTER_WEAPONS_LIST, connection)

char_weapons_list.weapons = char_weapons_list.weapons.apply(lambda x: x.split(','))
#print(char_weapons_list.to_json(orient='records'))

#print(rpg_tables['charactercreator_character'])
#print(char_items_list)
#print(char_weapons_list)

final_df = rpg_tables['charactercreator_character'].merge(char_items_list, on='character_id', how='left').merge(char_weapons_list, on='character_id', how='left').drop(columns='character_id')



#final_df.weapons = final_df.weapons.apply(lambda x: [] if x is NaN else x)

no_weapons = final_df.weapons.isnull()

final_df.weapons[no_weapons] = final_df.weapons[no_weapons].apply(lambda x: [])

final_df.num_weapons[no_weapons] = 0 #final_df.num_weapons[no_weapons].apply(lambda x: 0)

final_df.num_weapons = final_df.num_weapons.astype('int')

#print(final_df)

#print(rpg_tables['charactercreator_character_inventory'])

#print(rpg_tables['armory_item'])

#print(rpg_tables['armory_weapon'])

char_records = final_df.to_dict('records')

#Record/doc format:
#{
#  "name": <VALUE>,
#  "level": <VALUE>,
#  "exp": <VALUE>,
#  "hp": <VALUE>,
#  "strength": <VALUE>,
#  "intelligence": <VALUE>,
#  "dexterity": <VALUE>,
#  "wisdom": <VALUE>,
#  "num_items": <VALUE>,
#  "items": [
#    <ITEM NAME>,
#    <ITEM NAME>
#  ],
#  "num_weapons": <VALUE>,
#  "weapons" [
#    <ITEM NAME>,
#    <ITEM NAME>
#  ]
#}


#print(char_records)
#print(type(char_records))

passwd = getenv('PASSWD')
dbname = getenv('DBNAME')

client = pymongo.MongoClient(f"mongodb+srv://nsriniva:{passwd}@cluster0.vggnf.mongodb.net/{dbname}?retryWrites=true&w=majority")

print(client)
db = client.rpg

char_coll = db.characters

char_coll.insert_many(char_records)

for rpg_table in rpg_tables:
    db[rpg_table].insert_many(rpg_tables[rpg_table].to_dict('records'))

print(char_coll)


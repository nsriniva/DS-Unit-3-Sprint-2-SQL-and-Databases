import pymongo
from dotenv import load_dotenv
from os import getenv, path
import sqlite3
import pandas as pd
from numpy import NaN

load_dotenv()

passwd = getenv('PASSWD')
dbname = getenv('DBNAME')

client = pymongo.MongoClient(f"mongodb+srv://nsriniva:{passwd}@cluster0.vggnf.mongodb.net/{dbname}?retryWrites=true&w=majority")

#print(client)
db = client.rpg

char_coll = db.characters

total_chars = char_coll.count_documents({})

print(f'{total_chars = }')


total_items = db.armory_item.count_documents({})

print(f'{total_items = }')

total_weapons = db.armory_weapon.count_documents({})

print(f'{total_weapons = }')


total_non_weapons = total_items - total_weapons

print(f'{total_non_weapons = }')
items_per_char = list(char_coll.find({},{'name':1, 'num_items': 1, '_id':0}).limit(20))

print(f'{items_per_char = }')

weapons_per_char = list(char_coll.find({},{'name':1, 'num_weapons': 1, '_id':0}).limit(20))

print(f'{weapons_per_char = }')

# $group
#{
#  _id: 0,
#  avg_item: {
#    $avg: "$num_items"
#  }
#}

avg_items = list(
    char_coll.aggregate( 
    [{ 
    "$group" :  
        {"_id" : 1,  
         "avg_items" : {
             "$avg" : "$num_items"
             } 
         }} 
    ]) 
)[0]['avg_items']

print(f'{avg_items = }')

avg_weapons = list(
    char_coll.aggregate( 
    [{ 
    "$group" :  
        {"_id" : 1,  
         "avg_weapons" : {
             "$avg" : "$num_weapons"
             } 
         }} 
    ]) 
)[0]['avg_weapons']

print(f'{avg_weapons = }')


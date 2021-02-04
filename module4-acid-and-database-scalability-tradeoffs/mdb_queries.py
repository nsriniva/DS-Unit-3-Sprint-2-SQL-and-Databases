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

print(client)
db = client.rpg

char_coll = db.characters

print(char_coll)


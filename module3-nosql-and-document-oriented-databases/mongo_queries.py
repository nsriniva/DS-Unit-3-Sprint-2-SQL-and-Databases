import pymongo
from dotenv import load_dotenv
from os import getenv

load_dotenv()

passwd = getenv('PASSWD')
dbname = getenv('DBNAME')

print(passwd, dbname)

client = pymongo.MongoClient(f"mongodb+srv://nsriniva:{passwd}@cluster0.vggnf.mongodb.net/{dbname}?retryWrites=true&w=majority")

print(client)
db = client.test

print(db)
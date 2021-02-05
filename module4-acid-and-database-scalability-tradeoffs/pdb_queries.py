import os
from dotenv import load_dotenv
import psycopg2
from psycopg2 import extras
import json
import pandas as pd

load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")


connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
#print("CONNECTION", type(connection))

cursor = connection.cursor()
#print("CURSOR", type(cursor))

pdb_queries = {}

pdb_queries['NUM_SURVIVED'] = 'SELECT count(*) FROM titanic where survived=True'

pdb_queries['NUM_DIED'] = 'SELECT count(*) FROM titanic where survived=False'

pdb_queries['NUM_PASSENGERS_PER_CLASS'] = 'SELECT pclass, count(*) as num_passengers FROM titanic group by pclass order by pclass'

pdb_queries['SURVIVERS_PER_CLASS'] = 'SELECT pclass, count(*) as num_survivors FROM titanic where survived=True group by pclass order by pclass'

pdb_queries['DEAD_PER_CLASS'] = 'SELECT pclass, count(*) as num_survivors FROM titanic where survived=False group by pclass order by pclass'

pdb_queries['AVG_AGE_SURV_NSURV'] = 'SELECT survived, avg(age) as avg_age FROM titanic group by survived order by survived desc'

pdb_queries['AVG_AGE_PER_CLASS'] = 'SELECT pclass, avg(age) as avg_age FROM titanic group by pclass order by pclass'

pdb_queries['AVG_FARE_PER_CLASS'] = 'SELECT pclass, avg(fare) as avg_fare FROM titanic group by pclass order by pclass'

pdb_queries['AVG_FARE_SURV_NSURV'] = 'SELECT survived, avg(fare) as avg_fare FROM titanic group by survived order by survived desc'

pdb_queries['AVG_SISP_ABOARD_PER_CLASS'] = 'SELECT pclass, avg(si_sp_aboard) as avg_sisp_aboard FROM titanic group by pclass order by pclass'

pdb_queries['AVG_SISP_ABOARD_SURV_NSURV'] = 'SELECT survived, avg(si_sp_aboard) as avg_sisp_aboard FROM titanic group by survived order by survived desc'

pdb_queries['AVG_PACH_ABOARD_PER_CLASS'] = 'SELECT pclass, avg(pa_ch_aboard) as avg_pach_aboard FROM titanic group by pclass order by pclass'

pdb_queries['AVG_PACH_ABOARD_SURV_NSURV'] = 'SELECT survived, avg(pa_ch_aboard) as avg_pach_aboard FROM titanic group by survived order by survived desc'

pdb_queries['PASSENGER_SAME_NAME'] = 'SELECT foo.name, foo.num from (SELECT name, count(*) as num from titanic group by name) as foo where foo.num > 1'

single_num = ['NUM_SURVIVED', 'NUM_DIED']

for query_name, query in pdb_queries.items():
    cursor.execute(query)
    if query_name in single_num:
        print(f'{query_name} = {cursor.fetchone()[0]}')
    else:
        print(f'{query_name} = {cursor.fetchall()}')

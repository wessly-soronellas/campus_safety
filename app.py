import pymssql
import pandas as pd
import os
from dotenv import load_dotenv
from queries import VEHICLE_REGISTRATIONS


load_dotenv()
SERVER = os.getenv('SERVER')
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')
DATABASE = os.getenv('DATABASE_TEST')
print(SERVER)
conn = pymssql.connect(
    server=SERVER,
    user=USER,
    password=PASSWORD,
    database=DATABASE,
    as_dict=True
)

cursor = conn.cursor()
cursor.execute(VEHICLE_REGISTRATIONS)
records = cursor.fetchall()
df = pd.DataFrame(records)
df["license_plate"]= df["license_plate_state"] + "*" + df["license_plate"]
print(df)
from os import environ as env
from dotenv import load_dotenv
from sqlalchemy import create_engine, MetaData

load_dotenv()

print(env["DB_DATA"])

engine = create_engine(env["DB_DATA"])

meta = MetaData()

conn = engine.connect()
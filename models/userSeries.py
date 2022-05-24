from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import SmallInteger, VARCHAR
from config.db import meta

userSeries = Table("userSeries", meta, 
    Column("id_userSeries", SmallInteger, primary_key=True), 
    Column("id_usuario", SmallInteger),
    Column("id_serie", SmallInteger),
    Column("imagen", VARCHAR(1000)),
    )
from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import SmallInteger, VARCHAR
from config.db import meta

userSeries = Table("userSeries", meta, 
    Column("id_userSeries", SmallInteger, primary_key=True), 
    Column("id_usuario", SmallInteger),
    Column("id_serie", SmallInteger),
    Column("imagen", VARCHAR(1000)),
    )

watchingSeries = Table("watchingSeries", meta, 
    Column("id_watchingSerie", SmallInteger, primary_key=True), 
    Column("nombre_serie", VARCHAR(50)),
    Column("temporada", SmallInteger),
    Column("capitulo", SmallInteger),
    Column("imagen", VARCHAR(1000)),
    Column("id_usuario", SmallInteger),
    Column("id_serie", SmallInteger)
    )
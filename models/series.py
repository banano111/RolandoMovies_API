from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import VARCHAR, String, SmallInteger
from config.db import meta, engine

series = Table("series", meta, 
    Column("id_serie", SmallInteger, primary_key=True), 
    Column("nombre_serie", VARCHAR(40)),
    Column("genero", VARCHAR(20)),
    Column("descripcion", VARCHAR(500)),
    Column("imagen", VARCHAR(1000)),
    Column("calificacion", SmallInteger),
    Column("is_popular", SmallInteger),
    )
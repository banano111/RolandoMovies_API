from typing import Optional
from fastapi import APIRouter
from sqlalchemy.sql.expression import true
from sqlalchemy.sql.functions import user
from config.db import conn
from models.series import series
from models.userSeries import userSeries
from schemas.series import UserSerie


series_route = APIRouter(
    prefix="/series",
)

@series_route.get("/")
def get_series():
    series_db = conn.execute(series.select()).all()
    return series_db

@series_route.get("/userSeries/{user_id}")
def get_series(user_id):
    user_series = conn.execute(userSeries.select().where(userSeries.c.id_usuario == user_id)).all()
    return user_series

@series_route.post("/userSeries")
def create_sale(userSerie: UserSerie):
    print(userSerie)
    new_userSerie = userSerie.dict()
    result = conn.execute(userSeries.insert().values(new_userSerie))
    print(result)

    return {"userSeries_added": True}
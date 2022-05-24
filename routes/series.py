from typing import Optional
from fastapi import APIRouter
from sqlalchemy.sql.expression import true
from sqlalchemy.sql.functions import user
from config.db import conn
from models.series import series
from models.userSeries import userSeries, watchingSeries
from schemas.series import UserSerie, UserWatching


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

@series_route.get("/watching/{user_id}")
def getWatchingSeries(user_id):
    print(user_id)
    watching_series = conn.execute(watchingSeries.select().where(watchingSeries.c.id_usuario == user_id)).all()
    return watching_series

@series_route.post("/watching")
def create_sale(userWatching: UserWatching):
    print(userWatching)
    new_userUserWatching = userWatching.dict()
    result = conn.execute(watchingSeries.insert().values(new_userUserWatching))
    print(result)

    return {"userSeries_added": True}
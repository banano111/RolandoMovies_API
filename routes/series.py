from typing import Optional
from fastapi import APIRouter
from sqlalchemy.sql.expression import true
from sqlalchemy.sql.functions import user
from config.db import conn
from models.series import series


series_route = APIRouter(
    prefix="/series",
)

@series_route.get("/")
def get_series():
    series_db = conn.execute(series.select()).all()
    return series_db
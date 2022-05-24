from typing import Optional
from pydantic import BaseModel

class UserSerie(BaseModel):
    id_userSeries: Optional[int]
    id_usuario: int
    id_serie: int
    imagen: str
    class Config:
        orm_mode=True

class UserWatching(BaseModel):
    id_watchingSerie: Optional[int]
    nombre_serie: str
    temporada: str
    capitulo: str
    imagen: str
    id_usuario: int
    id_serie: int
    class Config:
        orm_mode=True
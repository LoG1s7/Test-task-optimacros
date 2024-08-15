from pydantic import BaseModel, confloat


class Coordinates(BaseModel):
    """
    Модель для хранения и валидации через Pydantic географических координат.
    """

    latitude: confloat(ge=-90, le=90)
    longitude: confloat(ge=-180, le=180)

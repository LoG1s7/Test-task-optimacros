from dadata import DadataAsync
from fastapi import HTTPException
from server.models import Coordinates
from server.settings import settings


async def get_address_by_coordinates(coordinates: Coordinates):
    """
    Асинхронная функция для получения адреса по координатам
    с помощью сервиса DaData.
    """
    try:
        async with DadataAsync(
            settings.API_TOKEN, settings.SECRET_KEY
        ) as dadata_client:
            address_data = await dadata_client.geolocate(
                name="address",
                lat=coordinates.latitude,
                lon=coordinates.longitude,
                count=1,
            )
            if not address_data:
                raise HTTPException(
                    status_code=404,
                    detail="Адрес не найден, попробуйте другие координаты",
                )
            full_address = address_data[0].get("unrestricted_value")
            components = address_data[0].get("data")
        return {
            "full_address": full_address,
            "region": components.get("region_with_type"),
            "area": components.get("area_with_type"),
            "settlement": components.get("settlement_with_type"),
            "city": components.get("city"),
            "street": components.get("street"),
            "house": components.get("house"),
            "postal_code": components.get("postal_code"),
            "kladr_code": components.get("kladr_id"),
            "fias_code": components.get("fias_id"),
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

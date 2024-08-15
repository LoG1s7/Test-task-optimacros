import logging

import uvicorn
from fastapi import FastAPI, Form, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import HTMLResponse
from server.models import Coordinates
from server.services import get_address_by_coordinates
from server.settings import TEMPLATES, settings
from starlette.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory=TEMPLATES)
logging.basicConfig(level=logging.INFO)


@app.exception_handler(HTTPException)
async def custom_http_exception_handler(request: Request, exc: HTTPException):
    """
    Обрабатывает исключения HTTPException, возвращая HTML-ответ с ошибкой.
    """
    return templates.TemplateResponse(
        request, "error.html", {"detail": exc.detail}
    )


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request):
    """
    Обрабатывает исключения, возникающие при валидации запроса.
    """
    return templates.TemplateResponse(
        request,
        "error.html",
        {
            "detail": "Некорректные данные, попытайтесь снова.",
        },
    )


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """
    Обрабатывает GET запросы к URL "/".

    Возвращает HTML ответ, отрендеренный из шаблона "form.html".
    """
    return templates.TemplateResponse(request, "form.html")


@app.post("/result", response_class=HTMLResponse)
async def get_result(
    request: Request, latitude: float = Form(...), longitude: float = Form(...)
):
    """
    Обрабатывает POST запросы к URL "/result".
    Ожидает два обязательных параметра: долготу и широту в формате float.
    Возвращает HTML ответ, отрендеренный из шаблона "result.html".
    В случае успеха возвращает найденный адрес по координатам,
    используя сервис DaData.
    В случае ошибки возвращает HTML страницу с информацией об ошибке.
    """
    coordinates = Coordinates(latitude=latitude, longitude=longitude)
    address_data = await get_address_by_coordinates(coordinates)
    try:
        return templates.TemplateResponse(
            request, "result.html", {**address_data}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    uvicorn.run(app, host=settings.HOST, port=settings.PORT)

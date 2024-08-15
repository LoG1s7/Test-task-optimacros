import unittest

from fastapi.testclient import TestClient
from main import app


class TestDaDataAPI(unittest.TestCase):
    def setUp(self):
        """
        Метод setUp вызывается перед запуском каждого теста.
        Он используется для инициализации атрибутов тестового класса.
        """
        self.client = TestClient(app)

    def test_home_page(self):
        """Проверяем стартовую страницу"""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Введите координаты", response.text)

    def test_valid_coordinates(self):
        """Проверяем ответы если координаты валидны"""
        longitude = "37.6173"
        latitude = "55.7558"  # Москва
        response = self.client.post(
            "/result", data={"longitude": longitude, "latitude": latitude}
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            "Адрес", response.text
        )  # Проверяем, что поле "Адрес" присутствует

    def test_invalid_coordinates(self):
        """Проверяем ответы если координаты невалидны"""
        response = self.client.post(
            "/result", data={"longitude": "0", "latitude": "0"}
        )  # Вносим невалидные широту и долготу
        self.assertIn(
            "Адрес не найден, попробуйте другие координаты",
            response.text
        )  # Проверяем наличие сообщения об ошибке


if __name__ == "__main__":
    unittest.main()

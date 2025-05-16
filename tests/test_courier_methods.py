import allure
import pytest

from data import DATA_FOR_CREATE_COURIER, EMPTY_DATA_FOR_CREATE_COURIER, DATA_WITHOUT_PASSWORD, DATA_WITHOUT_LOGIN, \
    INVALID_DATA_FOR_LOGIN_1, INVALID_DATA_FOR_LOGIN_2
from methods.courier_methods import CourierMethods
from helpers import data_for_courier

class TestCourierMethods:

    @allure.title('Тесты на проверку создания курьера')
    def test_create_courier(self):
        courier = CourierMethods()
        data = data_for_courier()
        code, response = courier.create_courier(data)
        assert code == 201 and response == {"ok": True}


    @allure.title('Тесты на проверку одинаковых курьеров')
    def test_create_same_couriers(self, courier):
        courier = CourierMethods()
        code, response  = courier.create_courier(DATA_FOR_CREATE_COURIER)
        assert code == 409 and response == {
        "code": 409,
        "message": "Этот логин уже используется. Попробуйте другой."
        }


    @allure.title('Тесты на проверку создания курьера без обязательных полей')
    def test_check_create_courier_without_required_fields(self):
        courier = CourierMethods()
        code, response = courier.create_courier(EMPTY_DATA_FOR_CREATE_COURIER)
        assert code == 400 and response == {
        "code": 400,
        "message": "Недостаточно данных для создания учетной записи"
        }


    @pytest.mark.parametrize(
        'data',
        [
            DATA_WITHOUT_LOGIN,
            DATA_WITHOUT_PASSWORD
        ]
    )
    def test_create_courier_without_one_field(self, data):
        allure.dynamic.title('Тестируем создание курьера без одного обязательного поля')
        courier = CourierMethods()
        code, response = courier.create_courier(data)
        assert code == 400 and response == {
            "code": 400,
            "message": "Недостаточно данных для создания учетной записи"
        }

    @allure.title('Тесты на проверку логина')
    def test_login_courier(self, courier):
        courier_login = CourierMethods()
        code, response = courier_login.login_courier(DATA_FOR_CREATE_COURIER)
        assert code == 200 and 'id' in response


    @allure.title('Тесты на проверку логина с некорректными данными')
    def test_login_courier_with_invalid_data(self, courier):
        courier_login = CourierMethods()
        data = data_for_courier()
        code, response = courier_login.login_courier(data)
        assert code == 404 and response == {
        "code": 404,
        "message": "Учетная запись не найдена"
        }

    @pytest.mark.parametrize(
        'data',
        [
            INVALID_DATA_FOR_LOGIN_1,
            INVALID_DATA_FOR_LOGIN_2
        ]
    )
    def test_login_courier_without_one_field(self, data):
        allure.dynamic.title('Тестируем логин без одного обязательного поля')
        courier = CourierMethods()
        code, response  = courier.login_courier(data)
        assert code == 400 and response == {
        "code": 400,
        "message": "Недостаточно данных для входа"
        }
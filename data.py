
# урлы запросов
BASE_URL = 'https://qa-scooter.praktikum-services.ru/api/v1/'
COURIER_URL = 'courier'
ORDER_URL = 'orders'

# корректные данные для создания курьера
DATA_FOR_CREATE_COURIER = {
    "login": "aliya.smith347",
    "password": "Aliya347!",
    "firstName": "Aliya"
}

# пустые данные для создания курьера
EMPTY_DATA_FOR_CREATE_COURIER = {
    "login": "",
    "password": "",
    "firstName": "Aliya"
}

# некорректные данные для логина
INVALID_DATA_FOR_LOGIN_1 = {
    "login": "",
    "password": "Aliya347!"
}

INVALID_DATA_FOR_LOGIN_2 = {
    "login": "aliya.smith347",
    "password": ""
}

#данные для логина без обязательных полей
DATA_WITHOUT_PASSWORD = {
    "login": "user1@gmail.com",
    "firstName": "Aliya"
}

DATA_WITHOUT_LOGIN = {
    "password": "userTest123",
    "firstName": "Aliya"
}

# базовый набор данных для создания заказа
BASE_ORDER_DATA = {
    "firstName": "Ivan",
    "lastName": "Ivanov",
    "address": "ул. Пушкина, дом 10",
    "metroStation": "5",
    "phone": "+7 999 123 45 67",
    "rentTime": 5,
    "deliveryDate": "2025-09-01",
    "comment": "Позвоните за час до доставки"
}

#цвета для заказа
BLACK_COLOR = 'BLACK'
GREY_COLOR = 'GREY'
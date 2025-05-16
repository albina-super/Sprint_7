import json
from json import loads

import requests
from allure import step

from data import BASE_URL, COURIER_URL


class CourierMethods:

    @step('Создаем курьера')
    def create_courier(self, params):
        response = requests.post(f'{BASE_URL}{COURIER_URL}', json=params)
        return response.status_code, loads(response.text)

    @step('Логинимся под курьером')
    def login_courier(self, params):
        response = requests.post(f'{BASE_URL}{COURIER_URL}/login', json=params)
        return response.status_code, loads(response.text)

    @step('Удаляем курьера')
    def delete_courier(self, courier_id):
        response = requests.delete(f'{BASE_URL}{COURIER_URL}/{courier_id}')
        return response



import requests

from data import BASE_URL, COURIER_URL


class CourierMethods:

    def create_courier(self, params):
        response = requests.post(f'{BASE_URL}{COURIER_URL}', json=params)
        return response.json()

    def login_courier(self, params):
        response = requests.post(f'{BASE_URL}{COURIER_URL}/login', json=params)
        return response.json()


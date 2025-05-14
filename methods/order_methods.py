import requests

from data import ORDER_URL, BASE_URL


class OrderMethods:

    def create_order(self, params):
        response = requests.post(f'{BASE_URL}{ORDER_URL}', json=params)
        return response.json()

    def get_list_orders(self, params):
        response = requests.get(f'{BASE_URL}{ORDER_URL}/list')
        return response.json()
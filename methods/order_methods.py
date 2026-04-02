import json
import requests
from data import Urls
import allure


class OrderMethods:

    def __init__(self):
        self.url = f'{Urls.BASE_URL}{Urls.ORDERS_URL}'

    @allure.step('Создание заказа')
    def post_order(self, order_data):
        response = requests.post(f'{self.url}', json=order_data)
        try:
            return response.status_code, response.json()
        except json.decoder.JSONDecodeError:
            return response.status_code, response.text

    @allure.step('Отмена заказа')
    def cancel_order(self, track):
        response = requests.put(f'{self.url}cancel/{track}')
        try:
            return response.status_code, response.json()
        except json.decoder.JSONDecodeError:
            return response.status_code, response.text

    @allure.step('Запрос списка заказов')
    def get_orders(self, params):
        response = requests.get(f'{self.url}', params=params)
        try:
            return response.status_code, response.json()
        except json.decoder.JSONDecodeError:
            return response.status_code, response.text
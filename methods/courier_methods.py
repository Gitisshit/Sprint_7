import allure
import requests
import json
from data import Urls
from faker import Faker


class CourierMethods:

    def __init__(self):
        self.url = f'{Urls.BASE_URL}{Urls.COURIERS_URL}'

    @allure.step('Создать курьера')
    def create_courier(self, params=None):
        if params is None:
            params = self.generate_courier_data()
        response = requests.post(f'{self.url}', data=params)
        params_for_login = {"login": params["login"], "password": params["password"]}
        try:
            return response.json(), response.status_code, params_for_login
        except json.decoder.JSONDecodeError:
            return response.text, response.status_code

    @allure.step('Авторизация курьера')
    def login_courier(self, params):
        response = requests.post(f'{self.url}{Urls.LOGIN_URL}', data=params)
        try:
            return response.json(), response.status_code
        except json.decoder.JSONDecodeError:
            return response.text, response.status_code

    @allure.step('Удалить курьера')
    def delete_courier(self, id):
        return requests.delete(f'{self.url}/{id}')

    @staticmethod
    def generate_courier_data():
        faker = Faker()
        fake_login = faker.user_name()
        fake_password = faker.password()
        fake_name = faker.name()
        return {'login': fake_login, 'password': fake_password, 'firstName': fake_name}

    def generate_courier_login(self):
        faker = Faker()
        return faker.user_name()
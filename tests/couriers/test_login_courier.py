import allure
import pytest
from data import MessageTexts
from data import Couriers


@allure.feature("Тесты авторизации курьеров")
class TestLoginCourier:

    @allure.title("Позитивный тест авторизации курьера")
    def test_login_courier_success(self, login_temp_courier):
        response, status_code = login_temp_courier
        assert status_code == 200 and isinstance(response['id'], int), \
            f'status_code: {status_code}, response: {response}'

    @allure.title("Негативный тест авторизации курьера без обязательных полей")
    @pytest.mark.parametrize("params", [{'login': '', 'password': ''},
                                        {'login': 'test_courier', 'password': ''},
                                        {'login': '', 'password': '1'}])
    def test_login_courier_with_incomplete_params_error(self, params, courier_methods):
        response, status_code = courier_methods.login_courier(params)
        assert status_code == 400 and response['message'] == MessageTexts.message_incomplete_courier_params_for_login,\
            f'status_code: {status_code}, response: {response}'

    @allure.title("Негативный тест авторизации курьера с некорректными данными")
    @pytest.mark.parametrize("params", [Couriers.existing_courier_wrong_login,
                                        Couriers.existing_courier_wrong_password])
    def test_login_courier_with_incorrect_params_error(self, params, courier_methods):
        response, status_code = courier_methods.login_courier(params)
        assert status_code == 404 and response['message'] == MessageTexts.message_not_exist_courier_params_for_login, \
            f'status_code: {status_code}, response: {response}'

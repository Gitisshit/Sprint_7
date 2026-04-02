from methods.courier_methods import CourierMethods
from data import Couriers, MessageTexts
import pytest
import allure


@allure.feature("Тесты создания курьеров")
class TestCreateCourier:

    @allure.title("Позитивный тест создания курьера")
    def test_create_courier_success_(self,create_temp_courier):
        response, status_code, _ = create_temp_courier
        assert status_code == 201 and response == MessageTexts.message_courier_created_successfully, \
            f'status_code: {status_code}, response: {response}'

    @allure.title("Негативный тест создания существующего курьера")
    def test_create_existing_courier_error(self, courier_methods):
        response, status_code, _ = courier_methods.create_courier(Couriers.existing_courier)
        assert status_code == 409 and response.get("message") == MessageTexts.message_existing_courier, \
            f'status_code: {status_code}, response: {response.get("message")}'

    @allure.title("Негативный тест создания курьера без обязательных полей")
    @pytest.mark.parametrize('params', [{'login': '', 'password': 'test123', 'firstName': 'testName'},
                                        {'login': CourierMethods().generate_courier_login(), 'password': '', 'firstName': 'testName'},
                                        {'login': CourierMethods().generate_courier_login(), 'password': 'test123', 'firstName': ''}])
    def test_create_courier_with_incomplete_params_error(self, params, courier_methods):
        response, status_code, _ = courier_methods.create_courier(params)
        assert status_code == 400 and response.get('message') == MessageTexts.message_incomplete_courier_params_for_creation, \
            f'status_code: {status_code}, response: {response.get('message')}'

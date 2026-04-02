import allure
import pytest
from data import Orders, MessageTexts


@allure.feature('Тесты создания заказов')
class TestCreateOrder:

    @allure.title('Позитивный тест создания заказа')
    @pytest.mark.parametrize('create_temp_order', [Orders.order_with_grey_scooter,
                                                   Orders.order_with_black_scooter,
                                                   Orders.order_with_black_and_grey_scooter,
                                                   Orders.order_without_colour_of_scooter], indirect=True)
    def test_create_order_success(self, create_temp_order):
        status_code, response = create_temp_order
        assert status_code == 201 and isinstance(response['track'], int), \
            f'status_code: {status_code}, response: {response}'

    @allure.title('Позитивный тест получения списка заказов')
    @pytest.mark.parametrize('get_order_list', [Orders.order_list_params_for_courier,
                                                Orders.order_list_params_avaluable_10,
                                                Orders.order_list_params_for_courier_metro_2,
                                                Orders.order_list_params_avaluable_10_metro], indirect=True)
    def test_get_order_list_success(self, get_order_list):
        status_code, response, _ = get_order_list
        assert status_code == 200 and isinstance(response['orders'], list), \
            f'status_code: {status_code}, response: {response}'

    @allure.title('Негативный тест получения списка заказов для несуществующего курьера')
    @pytest.mark.parametrize('get_order_list', [{'courierId': -1}, {'courierId': 0}], indirect=True)
    def test_get_order_list_with_not_existing_courier_error(self, get_order_list):
        status_code, response, courier_id = get_order_list
        assert (status_code == 404 and
                response['message'] == MessageTexts.message_get_order_with_not_existing_courier.format(courier_id)),\
            f'status_code: {status_code}, response: {response}'

import pytest
from methods.courier_methods import CourierMethods
from methods.order_methods import OrderMethods


@pytest.fixture()
def courier_methods():
    return CourierMethods()

@pytest.fixture()
def create_temp_courier():
    courier_methods = CourierMethods()
    response_data, status_code, params_for_login = courier_methods.create_courier()
    yield response_data, status_code, params_for_login
    courier_id = courier_methods.login_courier(params_for_login)[0]
    courier_methods.delete_courier(courier_id['id'])

@pytest.fixture()
def login_temp_courier(create_temp_courier):
    courier_methods = CourierMethods()
    courier_login_response = courier_methods.login_courier(create_temp_courier[2])
    return courier_login_response

@pytest.fixture()
def create_temp_order(request):
    order_data = request.param
    order_methods = OrderMethods()
    status_code, response = order_methods.post_order(order_data)
    yield status_code, response
    order_methods.cancel_order(response['track'])

@pytest.fixture()
def get_order_list(request):
    order_list_params = request.param
    order_methods = OrderMethods()
    status_code, response = order_methods.get_orders(order_list_params)
    courier_id = request.param.get('courierId')
    yield status_code, response, courier_id

import json


class Urls:
    BASE_URL = 'https://qa-scooter.praktikum-services.ru/api/v1/'
    ORDERS_URL = 'orders/'
    COURIERS_URL = 'courier/'
    LOGIN_URL = 'login/'

class Couriers:
    existing_courier = {"login": "test_fighter", "password": "1234"}
    existing_courier_id = {"id": 726573}
    existing_courier_wrong_login = {'login': 'wrong_fighter', "password": "1234"}
    existing_courier_wrong_password = {'login': "test_fighter", 'password': 'absolutely_wrong_password'}

class MessageTexts:
    message_courier_created_successfully = {"ok": True}
    message_existing_courier = 'Этот логин уже используется'
    message_incomplete_courier_params_for_creation = 'Недостаточно данных для создания учетной записи'
    message_incomplete_courier_params_for_login = 'Недостаточно данных для входа'
    message_not_exist_courier_params_for_login = 'Учетная запись не найдена'
    message_get_order_with_not_existing_courier = 'Курьер с идентификатором {} не найден'

class Orders:
    order_list_params_for_courier = {'courierId': Couriers.existing_courier_id['id']}
    order_list_params_avaluable_10 = {'limit': 10, 'page': 0}
    order_list_params_for_courier_metro_2 = {'courierId': Couriers.existing_courier_id['id'],
                                             'nearestStation': json.dumps(["110", "109"])}
    order_list_params_avaluable_10_metro = {'limit': 10, 'page': 0, 'nearestStation': ["110"]}
    order_list_params_for_not_existing_courier_metro_2 = {'courierId': 'no_id',
                                                          'nearestStation': json.dumps(["110", "109"])}

    order_with_black_scooter = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": ["BLACK"]}

    order_with_grey_scooter = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": ["GREY"]}

    order_with_black_and_grey_scooter = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": ["BLACK", "GREY"]}

    order_without_colour_of_scooter = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": []}


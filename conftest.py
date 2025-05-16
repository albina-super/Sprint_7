import pytest

from data import DATA_FOR_CREATE_COURIER, BASE_ORDER_DATA
from methods.courier_methods import CourierMethods


@pytest.fixture
def courier():
    courier = CourierMethods()
    code, response = courier.create_courier(DATA_FOR_CREATE_COURIER)
    yield response
    status, response_login = courier.login_courier(DATA_FOR_CREATE_COURIER)
    courier.delete_courier(response_login['id'])



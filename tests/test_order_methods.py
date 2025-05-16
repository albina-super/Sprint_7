import allure
import pytest

from data import BLACK_COLOR, GREY_COLOR, BASE_ORDER_DATA
from methods.order_methods import OrderMethods


class TestOrderMethods:

    @pytest.mark.parametrize("color", [
        [BLACK_COLOR],
        [GREY_COLOR],
        [GREY_COLOR, BLACK_COLOR],
        []
    ])
    def test_create_order(self, color):
        allure.dynamic.title('Тестируем создание заказами с разными полями "цвета"')
        order = OrderMethods()
        data = BASE_ORDER_DATA.copy()
        if color:
            data["color"] = color

        code, response = order.create_order(data)
        assert code == 201 and "track" in response


    @allure.title('Тесты на проверку получения списка заказов')
    def test_get_orders_list(self):
        orders = OrderMethods()
        code, response = orders.get_list_orders()
        assert code == 200 and isinstance(response["orders"], list) and  "orders" in response
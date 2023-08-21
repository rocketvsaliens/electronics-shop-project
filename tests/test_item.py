import pytest

from src.item import Item


@pytest.fixture
def item():
    return Item("Тестовый товар", 10.0, 5)


def test_calculate_total_price(item):
    assert item.calculate_total_price() == 50.0


def test_apply_discount(item):
    item.pay_rate = 0.8
    item.apply_discount()
    assert item.price == 8.0

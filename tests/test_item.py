import pytest

from src.item import Item


@pytest.fixture
def item():
    """Создаём тестовый экземпляр класса"""
    return Item("Тестовый товар", 10.0, 5)


def test_calculate_total_price(item):
    """Проверяем, что выводится общая стоимость товаров"""
    assert item.calculate_total_price() == 50.0


def test_apply_discount(item):
    """Проверяем, что устанавливается и применяется скидка на товар"""
    item.pay_rate = 0.8
    item.apply_discount()
    assert item.price == 8.0

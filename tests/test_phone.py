import pytest
from src.phone import Phone


@pytest.fixture
def phone():
    """Создаём тестовый экземпляр класса"""
    return Phone("iPhone 14", 120_000, 5, 2)


def test_str_repr(phone):
    assert repr(phone) == "Phone('iPhone 14', 120000, 5, 2)"
    assert str(phone) == 'iPhone 14'


def test_number_of_sim(phone):
    assert phone.number_of_sim == 2
    phone.number_of_sim = 1
    assert phone.number_of_sim == 1
    with pytest.raises(ValueError) as ex:
        phone.number_of_sim = 0
    assert str(ex.value) == 'Количество физических SIM-карт должно быть целым числом больше нуля.'


def test_invalid_number_of_sim():
    with pytest.raises(ValueError) as ex:
        obj = Phone('Test', 10.99, 5, -1)
    assert str(ex.value) == 'Количество физических SIM-карт должно быть целым числом больше нуля.'

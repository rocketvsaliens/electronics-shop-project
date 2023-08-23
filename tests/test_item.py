import pytest
import csv
import os

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


def test_name_setter(item):
    # Проверка установки корректного значения имени
    item.name = "Кварк"
    assert item.name == "Кварк"

    # Проверка обрезки имени, если оно превышает максимальную длину
    long_name = "Синхрофазатрон"
    item.name = long_name
    assert item.name == long_name[:Item.MAX_LENGTH]

    # Проверка установки пустого имени
    empty_name = ""
    item.name = empty_name
    assert item.name == empty_name

    # Проверка установки имени, которое в точности равно максимальной длине
    max_length_name = "A" * Item.MAX_LENGTH
    item.name = max_length_name
    assert item.name == max_length_name


@pytest.mark.parametrize("string, expected_result", [
    ("5", 5),
    ("5.0", 5),
    ("5.5", 5)
])
def test_string_to_number(string, expected_result):
    """
    Проверяем, что функция делает цифру из строки
    и возвращает исключение, если
    """
    assert Item.string_to_number(string) == expected_result
    with pytest.raises(ValueError):
        string = "test_string"
        Item.string_to_number(string)


def test_instantiate_from_csv():
    """
    Функция создаёт временный .csv файл.
    Проверяем корректность получения данных из .csv.
    Проверяем вызов исключения, если файл отсутствует или повреждён.
    """
    data = [
        {'name': 'item1', 'price': '10.0', 'quantity': '5'},
        {'name': 'item2', 'price': '15.0', 'quantity': '3'},
        {'name': 'item3', 'price': '20.0', 'quantity': '2'}
    ]
    with open('test.csv', 'w', encoding='cp1251', newline='') as file:
        fieldnames = ['name', 'price', 'quantity']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

    # Вызываем метод instantiate_from_csv()
    Item.PATH_TO_CSV = 'test.csv'
    Item.all = []
    Item.instantiate_from_csv()

    # Проверяем результаты
    assert len(Item.all) == 3
    assert Item.all[0].name == 'item1'
    assert Item.all[1].price == 15.0
    assert Item.all[2].quantity == 2

    # Удаляем временный .csv файл
    os.remove('test.csv')

    # Проверяем вызов исключения при отсутствии .csv файла
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv()

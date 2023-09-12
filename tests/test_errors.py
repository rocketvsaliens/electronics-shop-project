import pytest
import csv
import os

from src.item import Item
from src.errors import InstantiateCSVError


def test_instantiate_csv_error_exception():

    # Создаём неправильный временный файлик без одной колонки
    data = [
        {'name': 'item1', 'price': '10.0'},
        {'name': 'item2', 'price': '15.0'},
        {'name': 'item3', 'price': '20.0'}
    ]
    with open('test.csv', 'w', encoding='cp1251', newline='') as file:
        fieldnames = ['name', 'price']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    Item.PATH_TO_CSV = 'test.csv'

    # Вызываем исключение, т.к. в файле содержатся неправильные данные
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv()

    # Удаляем временный файлик
    os.remove('test.csv')

import os
import csv
from math import floor


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0  # процент скидки
    all = []  # список всех экземпляров класса
    MAX_NAME_LENGTH = 10  # максимальная длина поля name
    PATH_TO_CSV = os.path.join('src', 'items.csv')  # путь к файлу .csv

    @classmethod
    def instantiate_from_csv(cls):
        """
        Загружает экземпляры класса из .csv
        Если файла нет или он не читается, вызываем исключение FileNotFoundError
        """
        try:
            with open(cls.PATH_TO_CSV, encoding='cp1251') as file:
                reader = csv.DictReader(file)
                for line in reader:
                    item = cls(line['name'], float(line['price']), int(line['quantity']))
                    cls.all.append(item)
        except FileNotFoundError:
            raise FileNotFoundError('Файл отсутствует или поверждён')

    @staticmethod
    def string_to_number(string):
        """Переводит строку в целое число с округлением до меньшего значения"""
        if isinstance(string, str):
            try:
                return floor(float(string))
            except ValueError:
                raise ValueError('Строка не является числом')

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.
        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        # self.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) <= self.MAX_NAME_LENGTH:
            self.__name = name
        else:
            self.__name = name[:self.MAX_NAME_LENGTH]

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.
        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

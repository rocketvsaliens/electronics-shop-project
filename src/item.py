from src.errors import InstantiateCSVError
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
    PATH_TO_CSV = os.path.join('..', 'src', 'items.csv')  # путь к файлу .csv

    @classmethod
    def instantiate_from_csv(cls) -> None:
        """
        Загружает экземпляры класса из .csv
        Если файла нет или он не читается, вызываем исключение FileNotFoundError
        """
        try:
            with open(cls.PATH_TO_CSV, encoding='cp1251') as file:
                reader = csv.DictReader(file)
                cls.all.clear()
                for line in reader:
                    item = cls(line['name'], float(line['price']), int(line['quantity']))

        except FileNotFoundError:
            raise FileNotFoundError('Отсутствует файл item.csv')

        except KeyError:  # Выбросит исключение, т.к. нет ключа в словаре
            raise InstantiateCSVError('Файл item.csv поврежден')

    @staticmethod
    def string_to_number(string: str) -> int or ValueError:
        """Переводит строку в целое число с округлением до меньшего значения"""
        if isinstance(string, str):
            try:
                return floor(float(string))
            except ValueError:
                raise ValueError('Строка не является числом')

    def __init__(self, name: str, price: int or float, quantity: int) -> None:
        """
        Создание экземпляра класса item.
        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        super().__init__()
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __repr__(self) -> str:
        """Строковое представление объекта для разработчиков"""
        return f"Item('{self.name}', {self.price}, {self.quantity})"

    def __str__(self) -> str:
        """Пользовательское строковое представление объекта"""
        return self.name

    def __add__(self, other) -> int or Exception:
        """
        Складывает экземпляров класса Item и дочерних классов.
        Выбрасывает исключение, если один или оба операнда не экземпляры Item или дочерних классов.
        """
        if issubclass(other.__class__, self.__class__):
            return self.quantity + other.quantity
        else:
            raise Exception('Складывать можно только экземпляры одного класса или дочерних классов')

    @property
    def name(self) -> str:
        """Выводит название товара"""
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        """
        Задаёт новое название товара.
        Если название длиннее 10 символов, обрезает новое название до 10 символов
        """
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

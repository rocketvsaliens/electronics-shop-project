from src.item import Item


class Phone(Item):
    """
    Дочерний класс от Item для представления телефонов в магазине.
    """

    def __init__(self, name: str, price: int or float, quantity: int, number_of_sim: int) -> None:
        """
        Создание экземпляра класса item. Поля name, price quantity подтягиваются из родительского класса.
        :param number_of_sim: Количество сим-карт.
        """
        super().__init__(name, price, quantity)
        # Т.к. от int наследуется bool, то проверку на тип int лучше делать через type
        if type(number_of_sim) == int and number_of_sim > 0:
            self._number_of_sim = number_of_sim
        else:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')

    def __repr__(self) -> str:
        """Строковое представление объекта для разработчиков"""
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self._number_of_sim})"

    @property
    def number_of_sim(self) -> int:
        """Выводит количество сим-карт"""
        return self._number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, new_value: int):
        """
        Задаёт количество сим-карт. Количество сим-карт должно быть больше 0,
        иначе будет исключение ValueError.
        """
        # Т.к. от int наследуется bool, то проверку на тип int лучше делать через type
        if type(new_value) == int and new_value > 0:
            self._number_of_sim = new_value
        else:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')

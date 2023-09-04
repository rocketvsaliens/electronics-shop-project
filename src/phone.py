from src.item import Item


class Phone(Item):

    def __init__(self, name: str, price: int or float, quantity: int, number_of_sim: int) -> None:
        super().__init__(name, price, quantity)
        if type(number_of_sim) == int and number_of_sim > 0:
            self._number_of_sim = number_of_sim
        else:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self._number_of_sim})"

    @property
    def number_of_sim(self):
        return self._number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, new_value):
        if type(new_value) == int and new_value > 0:
            self._number_of_sim = new_value
        else:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')

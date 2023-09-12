class InstantiateCSVError(Exception):
    """
    Класс-исключение на случай, если файл csv поврежден
    (например, отсутствует одна из колонок данных)
    """
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
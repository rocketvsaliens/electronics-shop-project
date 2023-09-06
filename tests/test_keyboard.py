import pytest
from src.keyboard import Keyboard


@pytest.fixture
def keyboard():
    """Создаём тестовый экземпляр класса"""
    return Keyboard('Dark Project KD87A', 9600, 5)


def test_str(keyboard):
    assert str(keyboard) == "Dark Project KD87A"
    assert str(keyboard.language) == "EN"


def test_change_lang(keyboard):
    keyboard.change_lang()
    assert str(keyboard.language) == "RU"
    # Сделали RU -> EN -> RU
    keyboard.change_lang().change_lang()
    assert str(keyboard.language) == "RU"
    with pytest.raises(AttributeError):
        keyboard.language = 'CH'

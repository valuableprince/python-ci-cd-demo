import pytest
from calculator import calculate, divide

def test_addition():
    """Тест сложения"""
    assert calculate('+', 2, 3) == 5
    assert calculate('+', -1, 1) == 0
    assert calculate('+', 0, 0) == 0


def test_subtraction():
    """Тест вычитания"""
    assert calculate('-', 5, 3) == 2
    assert calculate('-', 0, 5) == -5


def test_multiplication():
    """Тест умножения"""
    assert calculate('*', 3, 4) == 12
    assert calculate('*', -2, 3) == -6


def test_division():
    """Тест деления"""
    assert calculate('/', 6, 2) == 3
    assert calculate('/', 5, 2) == 2.5


def test_division_by_zero():
    """Тест деления на ноль"""
    with pytest.raises(ValueError, match="Деление на ноль невозможно"):
        calculate('/', 5, 0)


def test_power():
    """Тест возведения в степень"""
    assert calculate('**', 2, 3) == 8
    assert calculate('**', 5, 0) == 1


def test_invalid_operation():
    """Тест неверной операции"""
    with pytest.raises(ValueError, match="Неподдерживаемая операция"):
        calculate('%', 5, 2)


def test_divide_function():
    """Отдельный тест функции divide"""
    assert divide(10, 2) == 5
    with pytest.raises(ValueError):
        divide(5, 0)
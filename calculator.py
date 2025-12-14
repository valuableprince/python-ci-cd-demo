"""
Простой калькулятор для демонстрации CI/CD
"""


def add(a: float, b: float) -> float:
    """Сложение"""
    return a + b


def subtract(a: float, b: float) -> float:
    """Вычитание"""
    return a - b


def multiply(a: float, b: float) -> float:
    """Умножение"""
    return a * b


def divide(a: float, b: float) -> float:
    """Деление"""
    if b == 0:
        raise ValueError("Деление на ноль невозможно")
    return a / b


def power(a: float, b: float) -> float:
    """Возведение в степень"""
    return a ** b


def calculate(operation: str, a: float, b: float) -> float:
    """Основная функция калькулятора"""
    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide,
        '**': power,
    }

    if operation not in operations:
        raise ValueError(f"Неподдерживаемая операция: {operation}")

    return operations[operation](a, b)


if __name__ == "__main__":
    print("Демонстрация работы калькулятора:")
    print(f"2 + 2 = {calculate('+', 2, 2)}")
    print(f"5 / 2 = {calculate('/', 5, 2)}")

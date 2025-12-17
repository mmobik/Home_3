import sys
import os
from io import StringIO
import random

# Добавляем путь к tasks для импорта функции
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from tasks.task_5 import lucky_tickets, main


def format_input(n: int, m: int) -> str:
    """Формирует строку входных данных."""
    return f"{n} {m}"


def calculate_result(n: int, m: int) -> int:
    """Вычисляет ожидаемый результат для теста."""
    old_stdin, old_stdout = sys.stdin, sys.stdout
    sys.stdin = StringIO(format_input(n, m))
    sys.stdout = StringIO()
    try:
        main()
        result_str = sys.stdout.getvalue().strip()
        return int(result_str)
    finally:
        sys.stdin, sys.stdout = old_stdin, old_stdout


def generate_test_case(n: int, m: int, description: str, expected: int | None = None) -> dict:
    """Создает тест-кейс с вычислением expected при необходимости."""
    if expected is None:
        expected = lucky_tickets(n, m)
    return {
        "N": n,
        "M": m,
        "description": description,
        "expected": expected,
        "time_limit": "2 секунды",
        "memory_limit": "64 мегабайта",
    }


# ========== ПРОСТЫЕ ТЕСТЫ (3) ==========
def test_case_1():
    """Минимальный M, кратчайший N."""
    return generate_test_case(
        n=2,
        m=2,
        description="Простой: N=2, M=2 (бинарные 2-значные)",
        expected=2,  # 00 и 11
    )


def test_case_2():
    """Короткий десятичный билет."""
    return generate_test_case(
        n=2,
        m=10,
        description="Простой: N=2, M=10 (2-значные десятичные)",
        expected=10,  # каждая цифра 0..9
    )


def test_case_3():
    """4-значный десятичный (классические)."""
    return generate_test_case(
        n=4,
        m=10,
        description="Простой: N=4, M=10",
    )


# ========== СРЕДНИЕ ТЕСТЫ (3) ==========
def test_case_4():
    """6-значный десятичный."""
    return generate_test_case(
        n=6,
        m=10,
        description="Средний: N=6, M=10",
    )


def test_case_5():
    """10-значный десятичный."""
    return generate_test_case(
        n=10,
        m=10,
        description="Средний: N=10, M=10",
    )


def test_case_6():
    """8-значный в максимальном основании."""
    return generate_test_case(
        n=8,
        m=26,
        description="Средний: N=8, M=26",
    )


# ========== БОЛЬШИЕ ТЕСТЫ (4) ==========
def test_case_7():
    """N=50, M=10."""
    return generate_test_case(
        n=50,
        m=10,
        description="Большой: N=50, M=10",
    )


def test_case_8():
    """Максимальный N при минимальном основании."""
    return generate_test_case(
        n=150,
        m=2,
        description="Большой: N=150, M=2 (минимальное основание)",
    )


def test_case_9():
    """Максимальный N при среднем основании."""
    return generate_test_case(
        n=150,
        m=10,
        description="Большой: N=150, M=10",
    )


def test_case_10():
    """Максимальный N и максимальное основание."""
    return generate_test_case(
        n=150,
        m=26,
        description="Большой: N=150, M=26 (максимальные значения)",
    )


def get_all_test_cases():
    """Возвращает все тест-кейсы."""
    return [
        test_case_1(),
        test_case_2(),
        test_case_3(),
        test_case_4(),
        test_case_5(),
        test_case_6(),
        test_case_7(),
        test_case_8(),
        test_case_9(),
        test_case_10(),
    ]


def format_test_case_input(test_case: dict) -> str:
    """Форматирует тест-кейс в строку входных данных."""
    return format_input(test_case["N"], test_case["M"])


import sys
import os
from io import StringIO

# Добавляем путь к tasks для импорта функции solve
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from tasks.task_6 import solve


def format_input(n: int, k: int) -> str:
    """Форматирует входные данные."""
    return f"{n}\n{k}"


def calculate_result(n: int, k: int) -> int:
    """Запускает solve() и возвращает числовой результат."""
    old_stdin, old_stdout = sys.stdin, sys.stdout
    sys.stdin = StringIO(format_input(n, k))
    sys.stdout = StringIO()
    try:
        solve()
        result_str = sys.stdout.getvalue().strip()
        return int(result_str)
    finally:
        sys.stdin, sys.stdout = old_stdin, old_stdout


def generate_test_case(n: int, k: int, description: str, expected: int | None = None) -> dict:
    """Создает тест-кейс, при необходимости вычисляет expected."""
    if expected is None:
        expected = calculate_result(n, k)
    return {
        "N": n,
        "K": k,
        "description": description,
        "expected": expected,
        "time_limit": "1 секунда",
        "memory_limit": "64 мегабайта",
    }


# ========== ПРОСТЫЕ ТЕСТЫ (3) ==========
def test_case_1():
    """Минимальные значения по условию: N=2, K=2."""
    return generate_test_case(
        n=2,
        k=2,
        description="Простой: N=2, K=2 (минимальные по условию)",
    )


def test_case_2():
    """Минимальный N, максимальный K."""
    return generate_test_case(
        n=2,
        k=10,
        description="Простой: N=2, K=10",
    )


def test_case_3():
    """Короткий, маленькое основание."""
    return generate_test_case(
        n=3,
        k=2,
        description="Простой: N=3, K=2",
    )


# ========== СРЕДНИЕ ТЕСТЫ (3) ==========
def test_case_4():
    """Средний размер, малое основание."""
    return generate_test_case(
        n=5,
        k=3,
        description="Средний: N=5, K=3",
    )


def test_case_5():
    """Средний размер, максимальное основание."""
    return generate_test_case(
        n=6,
        k=10,
        description="Средний: N=6, K=10",
    )


def test_case_6():
    """Средний размер, среднее основание."""
    return generate_test_case(
        n=8,
        k=5,
        description="Средний: N=8, K=5",
    )


# ========== БОЛЬШИЕ ТЕСТЫ (4) ==========
def test_case_7():
    """Большой N с минимальным основанием."""
    return generate_test_case(
        n=10,
        k=2,
        description="Большой: N=10, K=2",
    )


def test_case_8():
    """Большой N, максимальное основание при N+K<=18."""
    return generate_test_case(
        n=8,
        k=10,
        description="Большой: N=8, K=10 (N+K=18)",
    )


def test_case_9():
    """Почти максимум по сумме N+K."""
    return generate_test_case(
        n=12,
        k=6,
        description="Большой: N=12, K=6 (N+K=18)",
    )


def test_case_10():
    """Максимальный N при минимальном основании (быстрый рост)."""
    return generate_test_case(
        n=16,
        k=2,
        description="Большой: N=16, K=2 (N+K=18)",
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
    return format_input(test_case["N"], test_case["K"])


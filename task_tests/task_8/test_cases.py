import sys
import os
import random
from io import StringIO

# Добавляем путь к tasks для импорта функции main
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))
from tasks.task_8 import main


def format_input(n: int, points: list[tuple[int, int]]) -> str:
    lines = [str(n)]
    for x, y in points:
        lines.append(f"{x} {y}")
    return "\n".join(lines)


def calculate_result(n: int, points: list[tuple[int, int]]) -> str:
    old_stdin, old_stdout = sys.stdin, sys.stdout
    sys.stdin = StringIO(format_input(n, points))
    sys.stdout = StringIO()
    try:
        main()
        return sys.stdout.getvalue().strip()
    finally:
        sys.stdin, sys.stdout = old_stdin, old_stdout


def generate_test_case(n: int, points: list[tuple[int, int]], description: str, expected: str | None = None) -> dict:
    if expected is None:
        expected = calculate_result(n, points)
    return {
        "n": n,
        "points": points,
        "description": description,
        "expected": expected,
        "time_limit": "1 секунда",
        "memory_limit": "256 мегабайт",
    }


# ========== ПРОСТЫЕ ТЕСТЫ (3) ==========
def test_case_1():
    """Две точки, расстояние 5."""
    points = [(0, 0), (3, 4)]
    return generate_test_case(2, points, "Простой: 2 точки (расстояние 5.0000)", expected="5.0000")


def test_case_2():
    """Три точки на одной прямой с шагом 1."""
    points = [(0, 0), (0, 1), (0, 2)]
    return generate_test_case(3, points, "Простой: 3 точки на линии", expected="1.0000")


def test_case_3():
    """Квадрат 1x1, MST max edge = 1."""
    points = [(0, 0), (1, 0), (1, 1), (0, 1)]
    return generate_test_case(4, points, "Простой: квадрат 1x1", expected="1.0000")


# ========== СРЕДНИЕ ТЕСТЫ (3) ==========
def test_case_4():
    """Квадрат + диагональ: две пары близко, одна далеко."""
    points = [(0, 0), (0, 1), (1, 0), (10, 10)]
    return generate_test_case(4, points, "Средний: 2 кластера, связь ~14.1421")


def test_case_5():
    """Случайные 10 точек в пределах 0..10."""
    random.seed(42)
    points = [(random.randint(0, 10), random.randint(0, 10)) for _ in range(10)]
    return generate_test_case(10, points, "Средний: 10 случайных точек (0..10)")


def test_case_6():
    """Плотные точки + далекая одна, проверка длинной связи."""
    points = [(i, 0) for i in range(5)] + [(100, 100)]
    return generate_test_case(6, points, "Средний: 5 плотных + 1 далекая")


# ========== БОЛЬШИЕ ТЕСТЫ (4) ==========
def test_case_7():
    """Линия из 200 точек с шагом 1 (max edge = 1)."""
    points = [(i, 0) for i in range(200)]
    return generate_test_case(200, points, "Большой: линия 200 точек", expected="1.0000")


def test_case_8():
    """Кластер 500 точек в маленьком квадрате."""
    random.seed(123)
    points = [(random.randint(0, 50), random.randint(0, 50)) for _ in range(500)]
    return generate_test_case(500, points, "Большой: 500 точек в квадрате 0..50")


def test_case_9():
    """Две группы по 250, далеко друг от друга."""
    random.seed(321)
    group1 = [(random.randint(0, 10), random.randint(0, 10)) for _ in range(250)]
    group2 = [(random.randint(1000, 1010), random.randint(1000, 1010)) for _ in range(250)]
    points = group1 + group2
    return generate_test_case(500, points, "Большой: две далекие группы (500 точек)")


def test_case_10():
    """Максимум: 2000 точек на линии, шаг 1 (max edge = 1)."""
    points = [(i, 0) for i in range(2000)]
    return generate_test_case(2000, points, "Большой: линия 2000 точек", expected="1.0000")


def get_all_test_cases():
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
    return format_input(test_case["n"], test_case["points"])


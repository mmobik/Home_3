import sys
import os
from io import StringIO
import random

# Добавляем путь к tasks для импорта функции main
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))
from tasks.task_7 import main


def format_input(n: int, edges: list[tuple[int, int, int]]) -> str:
    """Форматирует входные данные."""
    lines = [f"{n} {len(edges)}"]
    for u, v, w in edges:
        lines.append(f"{u} {v} {w}")
    return "\n".join(lines)


def calculate_result(n: int, edges: list[tuple[int, int, int]]) -> str:
    """Запускает main() и возвращает строковый результат."""
    old_stdin, old_stdout = sys.stdin, sys.stdout
    sys.stdin = StringIO(format_input(n, edges))
    sys.stdout = StringIO()
    try:
        main()
        return sys.stdout.getvalue().strip()
    finally:
        sys.stdin, sys.stdout = old_stdin, old_stdout


def generate_test_case(n: int, edges: list[tuple[int, int, int]], description: str, expected: str | None = None) -> dict:
    """Создает тест-кейс, при необходимости вычисляет expected."""
    if expected is None:
        expected = calculate_result(n, edges)
    return {
        "n": n,
        "m": len(edges),
        "edges": edges,
        "description": description,
        "expected": expected,
        "time_limit": "1.3 секунды",
        "memory_limit": "64 мегабайта",
    }


# ========== ПРОСТЫЕ ТЕСТЫ (3) ==========
def test_case_1():
    """Минимально связный граф, ожидается вес 5."""
    n = 2
    edges = [(1, 2, 5)]
    return generate_test_case(n, edges, "Простой: n=2, m=1, связный", expected="5")


def test_case_2():
    """Несвязный граф без ребер."""
    n = 2
    edges = []
    return generate_test_case(n, edges, "Простой: n=2, m=0, несвязный", expected="Oops! I did it again")


def test_case_3():
    """Треугольник, выбираем максимальное остовное дерево."""
    n = 3
    edges = [(1, 2, 5), (2, 3, 4), (1, 3, 1)]
    return generate_test_case(n, edges, "Простой: n=3, треугольник", expected="9")


# ========== СРЕДНИЕ ТЕСТЫ (3) ==========
def test_case_4():
    """Квадрат с диагональю, максимальное остовное = 12."""
    n = 4
    edges = [
        (1, 2, 3),
        (2, 3, 2),
        (3, 4, 4),
        (4, 1, 1),
        (1, 3, 5),
    ]
    return generate_test_case(n, edges, "Средний: квадрат с диагональю", expected="12")


def test_case_5():
    """Мульти-ребра и петля, петля игнорируется."""
    n = 4
    edges = [
        (1, 1, 100),  # петля, должна быть проигнорирована
        (1, 2, 1),
        (1, 2, 3),   # кратное ребро, берем большее при сортировке
        (2, 3, 2),
        (3, 4, 4),
        (2, 4, 5),
    ]
    return generate_test_case(n, edges, "Средний: петля и кратные ребра", expected="12")


def test_case_6():
    """Несвязный граф из двух компонент."""
    n = 5
    edges = [
        (1, 2, 3),
        (2, 3, 2),
        (4, 5, 1),
    ]
    return generate_test_case(n, edges, "Средний: две компоненты", expected="Oops! I did it again")


# ========== БОЛЬШИЕ ТЕСТЫ (4) ==========
def test_case_7():
    """Полный граф на 5 вершинах со случайными весами."""
    random.seed(42)
    n = 5
    edges = []
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            w = random.randint(1, 100)
            edges.append((i, j, w))
    return generate_test_case(n, edges, "Большой: полный граф n=5")


def test_case_8():
    """n=10, разреженный граф."""
    random.seed(123)
    n = 10
    edges = []
    for _ in range(20):
        u = random.randint(1, n)
        v = random.randint(1, n)
        w = random.randint(0, 10000)
        edges.append((u, v, w))
    return generate_test_case(n, edges, "Большой: n=10, m=20 (разреженный)")


def test_case_9():
    """n=1000, m=0 — заведомо несвязный."""
    n = 1000
    edges = []
    return generate_test_case(n, edges, "Большой: n=1000, m=0, несвязный", expected="Oops! I did it again")


def test_case_10():
    """n=1000, случайные ребра (m=2000)."""
    random.seed(999)
    n = 1000
    edges = []
    for _ in range(2000):
        u = random.randint(1, n)
        v = random.randint(1, n)
        w = random.randint(0, 10000)
        edges.append((u, v, w))
    return generate_test_case(n, edges, "Большой: n=1000, m=2000 (случайный)")


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
    return format_input(test_case["n"], test_case["edges"])


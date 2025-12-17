import sys
import os
import random
from io import StringIO

# Добавляем путь к tasks для импорта функции solve
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))
from tasks.task_9 import solve


def format_input(n: int, m: int, k: int, diagonals: list[tuple[int, int]]) -> str:
    lines = [f"{n} {m}", str(k)]
    for x, y in diagonals:
        lines.append(f"{x} {y}")
    return "\n".join(lines)


def calculate_result(n: int, m: int, k: int, diagonals: list[tuple[int, int]]) -> str:
    old_stdin, old_stdout = sys.stdin, sys.stdout
    sys.stdin = StringIO(format_input(n, m, k, diagonals))
    sys.stdout = StringIO()
    try:
        solve()
        return sys.stdout.getvalue().strip()
    finally:
        sys.stdin, sys.stdout = old_stdin, old_stdout


def generate_test_case(n: int, m: int, diagonals: list[tuple[int, int]], description: str, expected: str | None = None) -> dict:
    k = len(diagonals)
    if expected is None:
        expected = calculate_result(n, m, k, diagonals)
    return {
        "N": n,
        "M": m,
        "K": k,
        "diagonals": diagonals,
        "description": description,
        "expected": expected,
        "time_limit": "1 секунда",
        "memory_limit": "64 мегабайта",
    }


# ========== ПРОСТЫЕ ТЕСТЫ (3) ==========
def test_case_1():
    """Без диагонали, минимальный размер 1x1."""
    return generate_test_case(
        n=1,
        m=1,
        diagonals=[],
        description="Простой: 1x1 без диагонали",
        expected="200",
    )


def test_case_2():
    """Диагональ доступна в единственном квартале 1x1."""
    return generate_test_case(
        n=1,
        m=1,
        diagonals=[(1, 1)],
        description="Простой: 1x1 с диагональю",
        expected=str(round(100 * (2 ** 0.5))),  # 141
    )


def test_case_3():
    """2x2 без диагоналей (макс ребро 100, итог 400)."""
    return generate_test_case(
        n=2,
        m=2,
        diagonals=[],
        description="Простой: 2x2 без диагоналей",
        expected="400",
    )


# ========== СРЕДНИЕ ТЕСТЫ (3) ==========
def test_case_4():
    """2x2 с диагоналями на (1,1) и (2,2)."""
    return generate_test_case(
        n=2,
        m=2,
        diagonals=[(1, 1), (2, 2)],
        description="Средний: 2x2 с диагоналями главной диагонали",
    )


def test_case_5():
    """3x3 без диагоналей (манхэттенский путь)."""
    return generate_test_case(
        n=3,
        m=3,
        diagonals=[],
        description="Средний: 3x3 без диагоналей",
        expected="600",
    )


def test_case_6():
    """3x3 с диагоналями (1,1),(2,2),(3,3)."""
    return generate_test_case(
        n=3,
        m=3,
        diagonals=[(1, 1), (2, 2), (3, 3)],
        description="Средний: 3x3 с диагоналями главной диагонали",
    )


# ========== БОЛЬШИЕ ТЕСТЫ (4) ==========
def test_case_7():
    """10x10 без диагоналей."""
    return generate_test_case(
        n=10,
        m=10,
        diagonals=[],
        description="Большой: 10x10 без диагоналей",
        expected="2000",
    )


def test_case_8():
    """10x10 с диагоналями вдоль главной диагонали (10 штук)."""
    diags = [(i, i) for i in range(1, 11)]
    return generate_test_case(
        n=10,
        m=10,
        diagonals=diags,
        description="Большой: 10x10 с диагоналями по главной",
    )


def test_case_9():
    """1000x1000 без диагоналей — максимальный размер без сокращений."""
    return generate_test_case(
        n=1000,
        m=1000,
        diagonals=[],
        description="Большой: 1000x1000 без диагоналей",
    )


def test_case_10():
    """30x40 со 100 случайными диагоналями."""
    random.seed(999)
    n, m = 30, 40
    diags = []
    for _ in range(100):
        x = random.randint(1, n)
        y = random.randint(1, m)
        diags.append((x, y))
    return generate_test_case(
        n=n,
        m=m,
        diagonals=diags,
        description="Большой: 30x40 со 100 случайными диагоналями",
    )


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
    return format_input(test_case["N"], test_case["M"], test_case["K"], test_case["diagonals"])


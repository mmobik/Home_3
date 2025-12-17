import random
import sys
import os
from io import StringIO

# Добавляем путь к tasks для импорта функции solve
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from tasks.task_10 import solve


def calculate_result(n, k, stations, matrix):
    """Вычисляет результат для заданных данных"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO(format_input(n, k, stations, matrix))
    sys.stdout = StringIO()
    
    try:
        solve()
        result_str = sys.stdout.getvalue().strip()
        result = int(result_str)
    finally:
        sys.stdin = old_stdin
        sys.stdout = old_stdout
    
    return result


def format_input(n, k, stations, matrix):
    """Форматирует входные данные"""
    lines = [f"{n} {k}"]
    lines.append(" ".join(map(str, stations)))
    for row in matrix:
        lines.append(" ".join(map(str, row)))
    return "\n".join(lines)


def generate_test_case(n, k, stations, matrix, description, expected=None):
    """Генерирует тест-кейс в формате для проверки
    
    Args:
        n: количество городов
        k: количество электростанций
        stations: список номеров городов с электростанциями (1-based)
        matrix: матрица стоимостей n×n
        description: описание теста
        expected: ожидаемый результат (если None, будет вычислен автоматически)
    """
    # Вычисляем expected если не указан
    if expected is None:
        expected = calculate_result(n, k, stations, matrix)
    
    test_case = {
        'n': n,
        'k': k,
        'stations': stations,
        'matrix': matrix,
        'description': description,
        'expected': expected,
        'time_limit': '1 секунда',
        'memory_limit': '64 мегабайт'
    }
    return test_case


def create_symmetric_matrix(n, min_val=1, max_val=100000):
    """Создает симметричную матрицу стоимостей"""
    random.seed(42)
    matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            val = random.randint(min_val, max_val)
            matrix[i][j] = val
            matrix[j][i] = val
    return matrix


# ========== ПРОСТЫЕ ТЕСТЫ (3 штуки) ==========

def test_case_1():
    """Простой тест: n=2, k=1, одна электростанция"""
    n = 2
    k = 1
    stations = [1]
    matrix = [
        [0, 10],
        [10, 0]
    ]
    # Минимальная стоимость: подключить город 2 к электростанции 1 = 10
    return generate_test_case(
        n=n,
        k=k,
        stations=stations,
        matrix=matrix,
        description="Простой тест: n=2, k=1, одна электростанция",
        expected=10
    )


def test_case_2():
    """Простой тест: n=3, k=1, все города связаны"""
    n = 3
    k = 1
    stations = [1]
    matrix = [
        [0, 5, 10],
        [5, 0, 3],
        [10, 3, 0]
    ]
    # Минимальная стоимость: 1->2 (5) + 2->3 (3) = 8
    return generate_test_case(
        n=n,
        k=k,
        stations=stations,
        matrix=matrix,
        description="Простой тест: n=3, k=1, все города связаны",
        expected=8
    )


def test_case_3():
    """Простой тест: n=3, k=2, две электростанции"""
    n = 3
    k = 2
    stations = [1, 2]
    matrix = [
        [0, 5, 10],
        [5, 0, 3],
        [10, 3, 0]
    ]
    # Минимальная стоимость: подключить город 3 к электростанции 2 = 3
    return generate_test_case(
        n=n,
        k=k,
        stations=stations,
        matrix=matrix,
        description="Простой тест: n=3, k=2, две электростанции",
        expected=3
    )


# ========== СРЕДНИЕ ТЕСТЫ (3 штуки) ==========

def test_case_4():
    """Средний тест: n=10, k=2, случайная матрица"""
    random.seed(123)
    n = 10
    k = 2
    stations = [1, 5]
    matrix = create_symmetric_matrix(n, min_val=1, max_val=1000)
    return generate_test_case(
        n=n,
        k=k,
        stations=stations,
        matrix=matrix,
        description="Средний тест: n=10, k=2, случайная матрица"
    )


def test_case_5():
    """Средний тест: n=20, k=5, случайная матрица"""
    random.seed(456)
    n = 20
    k = 5
    stations = [1, 5, 10, 15, 20]
    matrix = create_symmetric_matrix(n, min_val=1, max_val=5000)
    return generate_test_case(
        n=n,
        k=k,
        stations=stations,
        matrix=matrix,
        description="Средний тест: n=20, k=5, случайная матрица"
    )


def test_case_6():
    """Средний тест: n=50, k=1, одна электростанция"""
    random.seed(789)
    n = 50
    k = 1
    stations = [1]
    matrix = create_symmetric_matrix(n, min_val=1, max_val=10000)
    return generate_test_case(
        n=n,
        k=k,
        stations=stations,
        matrix=matrix,
        description="Средний тест: n=50, k=1, одна электростанция"
    )


# ========== БОЛЬШИЕ ТЕСТЫ (4 штуки) ==========

def test_case_7():
    """Большой тест: n=100, k=10, максимальный размер"""
    random.seed(999)
    n = 100
    k = 10
    stations = [1, 11, 21, 31, 41, 51, 61, 71, 81, 91]
    matrix = create_symmetric_matrix(n, min_val=1, max_val=100000)
    return generate_test_case(
        n=n,
        k=k,
        stations=stations,
        matrix=matrix,
        description="Большой тест: n=100, k=10, максимальный размер"
    )


def test_case_8():
    """Большой тест: n=100, k=1, одна электростанция, максимальные стоимости"""
    random.seed(111)
    n = 100
    k = 1
    stations = [1]
    matrix = create_symmetric_matrix(n, min_val=50000, max_val=100000)
    return generate_test_case(
        n=n,
        k=k,
        stations=stations,
        matrix=matrix,
        description="Большой тест: n=100, k=1, максимальные стоимости"
    )


def test_case_9():
    """Большой тест: n=100, k=50, половина городов - электростанции"""
    random.seed(222)
    n = 100
    k = 50
    stations = list(range(1, 51))  # города 1-50
    matrix = create_symmetric_matrix(n, min_val=1, max_val=100000)
    return generate_test_case(
        n=n,
        k=k,
        stations=stations,
        matrix=matrix,
        description="Большой тест: n=100, k=50, половина городов - электростанции"
    )


def test_case_10():
    """Большой тест: n=100, k=100, все города - электростанции"""
    random.seed(333)
    n = 100
    k = 100
    stations = list(range(1, 101))  # все города
    matrix = create_symmetric_matrix(n, min_val=1, max_val=100000)
    # Если все города - электростанции, стоимость = 0
    return generate_test_case(
        n=n,
        k=k,
        stations=stations,
        matrix=matrix,
        description="Большой тест: n=100, k=100, все города - электростанции",
        expected=0
    )


# ========== ФУНКЦИЯ ДЛЯ ПОЛУЧЕНИЯ ВСЕХ ТЕСТ-КЕЙСОВ ==========

def get_all_test_cases():
    """Возвращает все тест-кейсы"""
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


# ========== ФУНКЦИЯ ДЛЯ ФОРМАТИРОВАНИЯ ТЕСТ-КЕЙСА В ВХОДНОЙ ФОРМАТ ==========

def format_test_case_input(test_case):
    """Форматирует тест-кейс в формат входных данных"""
    n = test_case['n']
    k = test_case['k']
    stations = test_case['stations']
    matrix = test_case['matrix']
    return format_input(n, k, stations, matrix)


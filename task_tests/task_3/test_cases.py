import random
import sys
import os
from io import StringIO

# Добавляем путь к tasks для импорта функции main
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from tasks.task_3 import main


def calculate_result(N, talks):
    """Вычисляет результат для заданных докладов"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO(format_input(N, talks))
    sys.stdout = StringIO()
    
    try:
        main()
        result_str = sys.stdout.getvalue().strip()
        result = int(result_str)
    finally:
        sys.stdin = old_stdin
        sys.stdout = old_stdout
    
    return result


def format_input(N, talks):
    """Форматирует входные данные"""
    lines = [str(N)]
    for start, end in talks:
        lines.append(f"{start} {end}")
    return "\n".join(lines)


def generate_test_case(N, talks, description, expected=None):
    """Генерирует тест-кейс в формате для проверки
    
    Args:
        N: количество докладов
        talks: список кортежей (Ts, Te) - время начала и окончания
        description: описание теста
        expected: ожидаемый результат (если None, будет вычислен автоматически)
    """
    # Вычисляем expected если не указан
    if expected is None:
        expected = calculate_result(N, talks)
    
    test_case = {
        'N': N,
        'talks': talks,
        'description': description,
        'expected': expected,
        'time_limit': '1 секунда',
        'memory_limit': '64 мегабайт'
    }
    return test_case


# ========== ПРОСТЫЕ ТЕСТЫ (3 штуки) ==========

def test_case_1():
    """Простой тест: один доклад"""
    # N=1, один доклад (1, 5) -> можно посетить 1 доклад
    return generate_test_case(
        N=1,
        talks=[(1, 5)],
        description="Простой тест: один доклад",
        expected=1
    )


def test_case_2():
    """Простой тест: все доклады можно посетить"""
    # N=3, доклады не пересекаются и разделены хотя бы одной минутой
    # (1, 5), (6, 10), (11, 15) -> можно посетить все 3
    return generate_test_case(
        N=3,
        talks=[(1, 5), (6, 10), (11, 15)],
        description="Простой тест: все доклады можно посетить (не пересекаются)",
        expected=3
    )


def test_case_3():
    """Простой тест: доклады пересекаются, можно посетить только один"""
    # N=3, все доклады пересекаются: (1, 10), (2, 11), (3, 12)
    # Можно посетить только один (первый по окончанию) -> 1
    return generate_test_case(
        N=3,
        talks=[(1, 10), (2, 11), (3, 12)],
        description="Простой тест: все доклады пересекаются, можно посетить только один",
        expected=1
    )


# ========== СРЕДНИЕ ТЕСТЫ (3 штуки) ==========

def test_case_4():
    """Средний тест: 10 докладов, некоторые пересекаются"""
    random.seed(42)
    talks = []
    for i in range(10):
        start = random.randint(1, 20)
        end = random.randint(start + 1, 30)
        talks.append((start, end))
    return generate_test_case(
        N=10,
        talks=talks,
        description="Средний тест: 10 докладов, случайные времена"
    )


def test_case_5():
    """Средний тест: 50 докладов, последовательные интервалы"""
    talks = []
    for i in range(50):
        start = i * 2 + 1  # 1, 3, 5, 7, ...
        end = start + 1     # 2, 4, 6, 8, ...
        talks.append((start, end))
    return generate_test_case(
        N=50,
        talks=talks,
        description="Средний тест: 50 докладов, последовательные интервалы"
    )


def test_case_6():
    """Средний тест: 100 докладов, чередование пересекающихся и непересекающихся"""
    talks = []
    for i in range(100):
        if i % 2 == 0:
            # Четные - непересекающиеся
            start = i * 5 + 1
            end = start + 2
        else:
            # Нечетные - пересекающиеся с предыдущим
            start = i * 5 - 1
            end = start + 2
        talks.append((start, end))
    return generate_test_case(
        N=100,
        talks=talks,
        description="Средний тест: 100 докладов, чередование пересекающихся и непересекающихся"
    )


# ========== БОЛЬШИЕ ТЕСТЫ (4 штуки) ==========

def test_case_7():
    """Большой тест: максимальное количество докладов (N=100000)"""
    random.seed(123)
    talks = []
    for i in range(100000):
        start = random.randint(1, 29999)
        end = random.randint(start + 1, 30000)
        talks.append((start, end))
    return generate_test_case(
        N=100000,
        talks=talks,
        description="Большой тест: максимальное количество докладов N=100000, случайные времена"
    )


def test_case_8():
    """Большой тест: граничные значения времени (минимальные)"""
    random.seed(456)
    talks = []
    for i in range(10000):
        # Минимальные времена: Ts=1, Te близко к 1
        start = 1
        end = random.randint(2, 10)
        talks.append((start, end))
    return generate_test_case(
        N=10000,
        talks=talks,
        description="Большой тест: граничные значения времени (минимальные, Ts=1)"
    )


def test_case_9():
    """Большой тест: граничные значения времени (максимальные)"""
    random.seed(789)
    talks = []
    for i in range(10000):
        # Максимальные времена: Te=30000, Ts близко к 30000
        end = 30000
        start = random.randint(29990, 29999)
        talks.append((start, end))
    return generate_test_case(
        N=10000,
        talks=talks,
        description="Большой тест: граничные значения времени (максимальные, Te=30000)"
    )


def test_case_10():
    """Большой тест: максимальный N=100000 с экстремальными значениями"""
    random.seed(999)
    talks = []
    for i in range(100000):
        # Чередуем разные диапазоны времен
        if i % 4 == 0:
            # Минимальные времена
            start = 1
            end = random.randint(2, 100)
        elif i % 4 == 1:
            # Средние времена
            start = random.randint(10000, 20000)
            end = random.randint(start + 1, start + 100)
        elif i % 4 == 2:
            # Высокие времена
            start = random.randint(25000, 29900)
            end = random.randint(start + 1, 30000)
        else:
            # Максимальные времена
            start = random.randint(29950, 29999)
            end = 30000
        talks.append((start, end))
    return generate_test_case(
        N=100000,
        talks=talks,
        description="Большой тест: максимальный N=100000 с различными значениями времен"
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
    N = test_case['N']
    talks = test_case['talks']
    return format_input(N, talks)


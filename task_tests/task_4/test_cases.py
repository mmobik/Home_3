import random
import sys
import os
from io import StringIO

# Добавляем путь к tasks для импорта функции main
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from tasks.task_4 import main, can_split


def calculate_result(n, arr):
    """Вычисляет результат для заданного массива"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO(format_input(n, arr))
    sys.stdout = StringIO()
    
    try:
        main()
        result_str = sys.stdout.getvalue().strip()
        result = result_str == "True"
    finally:
        sys.stdin = old_stdin
        sys.stdout = old_stdout
    
    return result


def format_input(n, arr):
    """Форматирует входные данные"""
    if n == 0:
        return "0\n\n"  # Пустая строка для массива (n=0), но все равно нужна вторая строка
    return f"{n}\n{' '.join(map(str, arr))}"


def generate_test_case(n, arr, description, expected=None):
    """Генерирует тест-кейс в формате для проверки
    
    Args:
        n: количество чисел
        arr: список чисел (очки)
        description: описание теста
        expected: ожидаемый результат (если None, будет вычислен автоматически)
    """
    # Вычисляем expected если не указан
    if expected is None:
        expected = calculate_result(n, arr)
    
    test_case = {
        'n': n,
        'arr': arr,
        'description': description,
        'expected': expected,
        'time_limit': '1.5 секунды',
        'memory_limit': '8 мегабайт'
    }
    return test_case


# ========== ПРОСТЫЕ ТЕСТЫ (3 штуки) ==========

def test_case_1():
    """Простой тест: пустой массив (n=0)"""
    return generate_test_case(
        n=0,
        arr=[],
        description="Простой тест: пустой массив (n=0)",
        expected=True  # Пустой массив можно разбить на две пустые части
    )


def test_case_2():
    """Простой тест: один элемент"""
    # n=1, arr=[5] -> сумма 5, нельзя разбить на две равные части
    return generate_test_case(
        n=1,
        arr=[5],
        description="Простой тест: один элемент, нельзя разбить",
        expected=False
    )


def test_case_3():
    """Простой тест: можно разбить"""
    # n=4, arr=[1, 1, 2, 2] -> сумма 6, можно разбить на [1,2] и [1,2]
    return generate_test_case(
        n=4,
        arr=[1, 1, 2, 2],
        description="Простой тест: можно разбить на две равные части",
        expected=True
    )


# ========== СРЕДНИЕ ТЕСТЫ (3 штуки) ==========

def test_case_4():
    """Средний тест: n=30, случайные числа"""
    random.seed(42)
    arr = [random.randint(1, 300) for _ in range(30)]
    # Проверяем, можно ли разбить
    total = sum(arr)
    if total % 2 != 0:
        # Если сумма нечетная, нельзя разбить - делаем четную
        arr[-1] = arr[-1] + 1 if arr[-1] < 300 else arr[-1] - 1
    return generate_test_case(
        n=30,
        arr=arr,
        description="Средний тест: n=30, случайные числа"
    )


def test_case_5():
    """Средний тест: n=100, можно разбить"""
    random.seed(123)
    # Создаем массив, который точно можно разбить
    # Берем пары чисел, которые дают одинаковую сумму
    arr = []
    for i in range(50):
        val = random.randint(1, 300)
        arr.extend([val, val])  # Добавляем два одинаковых числа
    return generate_test_case(
        n=100,
        arr=arr,
        description="Средний тест: n=100, можно разбить (пары одинаковых чисел)"
    )


def test_case_6():
    """Средний тест: n=150, нельзя разбить"""
    random.seed(456)
    arr = [random.randint(1, 300) for _ in range(150)]
    # Делаем сумму нечетной, чтобы нельзя было разбить
    total = sum(arr)
    if total % 2 == 0:
        arr[0] = arr[0] + 1 if arr[0] < 300 else arr[0] - 1
    return generate_test_case(
        n=150,
        arr=arr,
        description="Средний тест: n=150, нельзя разбить (нечетная сумма)"
    )


# ========== БОЛЬШИЕ ТЕСТЫ (4 штуки) ==========

def test_case_7():
    """Большой тест: n=200, случайные числа"""
    random.seed(789)
    arr = [random.randint(1, 300) for _ in range(200)]
    return generate_test_case(
        n=200,
        arr=arr,
        description="Большой тест: n=200, случайные числа"
    )


def test_case_8():
    """Большой тест: n=250, можно разбить"""
    random.seed(999)
    # Создаем массив, который можно разбить
    arr = []
    for i in range(125):
        val = random.randint(1, 300)
        arr.extend([val, val])
    return generate_test_case(
        n=250,
        arr=arr,
        description="Большой тест: n=250, можно разбить (пары одинаковых чисел)"
    )


def test_case_9():
    """Большой тест: n=300, максимальный размер, случайные числа"""
    random.seed(111)
    arr = [random.randint(1, 300) for _ in range(300)]
    return generate_test_case(
        n=300,
        arr=arr,
        description="Большой тест: n=300, максимальный размер, случайные числа"
    )


def test_case_10():
    """Большой тест: n=300, максимальные значения (все числа = 300)"""
    # Все числа максимальные (300), сумма = 300 * 300 = 90000
    # 90000 четное, можно разбить на две части по 45000
    arr = [300] * 300
    return generate_test_case(
        n=300,
        arr=arr,
        description="Большой тест: n=300, все числа максимальные (300)",
        expected=True  # 300*300 = 90000, четное, можно разбить
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
    arr = test_case['arr']
    return format_input(n, arr)

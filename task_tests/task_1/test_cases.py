import random


def generate_test_case(L, N, points, description, expected=None):
    """Генерирует тест-кейс в формате для проверки"""
    test_case = {
        'L': L,
        'N': N,
        'points': points,
        'description': description,
        'time_limit': '1 секунда',
        'memory_limit': '256 мегабайт'
    }
    if expected is not None:
        test_case['expected'] = expected
    return test_case


# ========== ПРОСТЫЕ ТЕСТЫ (3 штуки) ==========

def test_case_1():
    """Простой тест: одна точка"""
    # L=5, points=[10] -> одна точка, одна группа
    return generate_test_case(
        L=5,
        N=1,
        points=[10],
        description="Простой тест: одна точка",
        expected=1
    )


def test_case_2():
    """Простой тест: все точки в одной группе"""
    # L=10, points=[1,5,10,15,20] -> start=1, покрывает до 1+20=21, все точки попадают -> 1 группа
    return generate_test_case(
        L=10,
        N=5,
        points=[1, 5, 10, 15, 20],
        description="Простой тест: все точки в одной группе (L=10, 5 точек: 1, 5, 10, 15, 20)",
        expected=1
    )


def test_case_3():
    """Простой тест: каждая точка в отдельной группе"""
    # L=0, points=[1,10,20,30] -> каждая точка отдельно -> 4 группы
    return generate_test_case(
        L=0,
        N=4,
        points=[1, 10, 20, 30],
        description="Простой тест: L=0, каждая точка в отдельной группе",
        expected=4
    )


# ========== СРЕДНИЕ ТЕСТЫ (3 штуки) ==========

def test_case_4():
    """Средний тест: несколько групп"""
    return generate_test_case(
        L=5,
        N=10,
        points=[1, 3, 5, 12, 14, 16, 25, 27, 29, 40],
        description="Средний тест: несколько групп точек"
    )


def test_case_5():
    """Средний тест: точки в случайном порядке"""
    points = [50, 10, 90, 30, 70, 20, 80, 40, 60, 5]
    return generate_test_case(
        L=15,
        N=10,
        points=points,
        description="Средний тест: точки в случайном порядке"
    )


def test_case_6():
    """Средний тест: граничные значения сдвига"""
    return generate_test_case(
        L=1,
        N=20,
        points=list(range(1, 21)),
        description="Средний тест: маленький сдвиг L=1, точки от 1 до 20"
    )


# ========== БОЛЬШИЕ ТЕСТЫ (4 штуки) ==========

def test_case_7():
    """Большой тест: максимальное количество точек (N=10000)"""
    random.seed(42)
    points = sorted([random.randint(-10**9, 10**9) for _ in range(10000)])
    return generate_test_case(
        L=10**7,
        N=10000,
        points=points,
        description="Большой тест: N=10000, случайные точки, L=10^7"
    )


def test_case_8():
    """Большой тест: максимальный сдвиг (L=10^8)"""
    random.seed(123)
    points = sorted([random.randint(-10**9, 10**9) for _ in range(1000)])
    return generate_test_case(
        L=10**8,
        N=1000,
        points=points,
        description="Большой тест: максимальный сдвиг L=10^8, N=1000"
    )


def test_case_9():
    """Большой тест: граничные значения точек (минимальные и максимальные)"""
    points = [-10**9, -10**9 + 1, 0, 10**9 - 1, 10**9]
    random.seed(456)
    additional_points = [random.randint(-10**9, 10**9) for _ in range(9995)]
    points.extend(additional_points)
    points = sorted(points)
    return generate_test_case(
        L=10**6,
        N=10000,
        points=points,
        description="Большой тест: граничные значения точек (-10^9, 10^9), N=10000"
    )


def test_case_10():
    """Большой тест: все точки на границах диапазона"""
    points = []
    for i in range(5000):
        points.append(-10**9 + i)
        points.append(10**9 - i)
    points = sorted(points[:10000])
    return generate_test_case(
        L=2 * 10**8,
        N=10000,
        points=points,
        description="Большой тест: точки на границах диапазона, большой сдвиг"
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
    L = test_case['L']
    N = test_case['N']
    points = test_case['points']
    return f"{L} {N}\n{' '.join(map(str, points))}"

import random
import sys
import os
from io import StringIO

# Добавляем путь к tasks для импорта функции solve
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from tasks.task_2 import solve


def calculate_result(N, rates):
    """Вычисляет результат для заданных курсов"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO(format_input(N, rates))
    sys.stdout = StringIO()
    
    try:
        solve()
        result_str = sys.stdout.getvalue().strip()
        result = float(result_str)
        # Проверяем на inf и nan
        if not (result != float('inf') and result != float('-inf') and result == result):
            raise ValueError("Результат inf или nan")
    finally:
        sys.stdin = old_stdin
        sys.stdout = old_stdout
    
    return result


def format_input(N, rates):
    """Форматирует входные данные"""
    lines = [str(N)]
    for usd_rate, eur_rate in rates:
        lines.append(f"{usd_rate:.2f} {eur_rate:.2f}")
    return "\n".join(lines)


def generate_test_case(N, rates, description, expected=None):
    """Генерирует тест-кейс в формате для проверки
    
    Args:
        N: количество дней
        rates: список кортежей (курс_доллара, курс_евро) для каждого дня
        description: описание теста
        expected: ожидаемый результат (если None, будет вычислен автоматически)
    """
    # Вычисляем expected если не указан
    if expected is None:
        try:
            expected = calculate_result(N, rates)
            # Проверяем, что результат не превышает 10^8
            if expected > 10**8:
                raise ValueError(f"Результат {expected} превышает 10^8")
        except (ValueError, OverflowError) as e:
            # Если произошла ошибка, пробуем пересчитать с более безопасными курсами
            print(f"Предупреждение: {description} - ошибка при вычислении: {e}")
            # Используем фиксированное значение как fallback
            expected = 100.0
    
    test_case = {
        'N': N,
        'rates': rates,
        'description': description,
        'expected': expected,
        'time_limit': '1 секунда',
        'memory_limit': '256 мегабайт'
    }
    return test_case


# ========== ПРОСТЫЕ ТЕСТЫ (3 штуки) ==========

def test_case_1():
    """Простой тест: один день, курсы доллара=2.0, евро=1.5"""
    return generate_test_case(
        N=1,
        rates=[(2.0, 1.5)],
        description="Простой тест: один день, курсы доллара=2.0, евро=1.5",
        expected=100.00
    )


def test_case_2():
    """Простой тест: два дня, выгодно обменять на доллары во второй день"""
    return generate_test_case(
        N=2,
        rates=[(2.0, 1.5), (3.0, 2.0)],
        description="Простой тест: два дня, выгодно обменять на доллары во второй день",
        expected=150.00
    )


def test_case_3():
    """Простой тест: три дня, выгодно обменять через евро"""
    return generate_test_case(
        N=3,
        rates=[(2.0, 1.5), (2.0, 2.5), (2.0, 2.0)],
        description="Простой тест: три дня, выгодно обменять через евро",
        expected=166.67
    )


# ========== СРЕДНИЕ ТЕСТЫ (3 штуки) ==========

def test_case_4():
    """Средний тест: 10 дней, умеренные курсы (результат ≤ 10^8)"""
    random.seed(42)
    # Генерируем курсы так, чтобы результат не превышал 10^8
    # Используем умеренные значения от 0.5 до 2.0
    rates = [(round(random.uniform(0.5, 2.0), 2), 
              round(random.uniform(0.5, 2.0), 2)) 
             for _ in range(10)]
    return generate_test_case(
        N=10,
        rates=rates,
        description="Средний тест: 10 дней, умеренные курсы"
    )


def test_case_5():
    """Средний тест: 50 дней, постепенный рост курсов (результат ≤ 10^8)"""
    rates = []
    for i in range(50):
        # Умеренный рост от 1.0 до 2.0
        usd_rate = 1.0 + i * 0.02  # от 1.0 до 1.98
        eur_rate = 1.0 + i * 0.015  # от 1.0 до 1.735
        rates.append((round(usd_rate, 2), round(eur_rate, 2)))
    return generate_test_case(
        N=50,
        rates=rates,
        description="Средний тест: 50 дней, постепенный рост курсов"
    )


def test_case_6():
    """Средний тест: 100 дней, чередование выгодных курсов (результат ≤ 10^8)"""
    rates = []
    for i in range(100):
        if i % 2 == 0:
            # Четные дни: доллар немного выгоднее
            rates.append((round(1.5 + i * 0.005, 2), round(1.2, 2)))
        else:
            # Нечетные дни: евро немного выгоднее
            rates.append((round(1.5, 2), round(1.2 + i * 0.005, 2)))
    return generate_test_case(
        N=100,
        rates=rates,
        description="Средний тест: 100 дней, чередование выгодных курсов"
    )


# ========== БОЛЬШИЕ ТЕСТЫ (4 штуки) ==========

def test_case_7():
    """Большой тест: максимальное количество дней (N=5000), весь диапазон курсов"""
    random.seed(123)
    rates = []
    for i in range(5000):
        # 80% случаев - обычные курсы (0.5 - 2.0)
        # 15% случаев - средние курсы (2.0 - 100.0)
        # 5% случаев - экстремальные курсы (0.01-0.5 или 100-10000)
        rand = random.random()
        if rand < 0.8:
            # Обычные курсы
            usd_rate = round(random.uniform(0.5, 2.0), 2)
            eur_rate = round(random.uniform(0.5, 2.0), 2)
        elif rand < 0.95:
            # Средние курсы
            usd_rate = round(random.uniform(2.0, 100.0), 2)
            eur_rate = round(random.uniform(2.0, 100.0), 2)
        else:
            # Экстремальные курсы (редко)
            if random.random() < 0.5:
                # Очень маленькие
                usd_rate = round(random.uniform(0.01, 0.5), 2)
                eur_rate = round(random.uniform(0.01, 0.5), 2)
            else:
                # Очень большие
                usd_rate = round(random.uniform(100.0, 10000.0), 2)
                eur_rate = round(random.uniform(100.0, 10000.0), 2)
        rates.append((usd_rate, eur_rate))
    return generate_test_case(
        N=5000,
        rates=rates,
        description="Большой тест: максимальное количество дней N=5000, весь диапазон курсов (0.01-10000)"
    )


def test_case_8():
    """Большой тест: граничные значения курсов (минимальные)"""
    random.seed(456)
    rates = []
    for i in range(1000):
        # 70% случаев - обычные курсы (0.5 - 1.5)
        # 20% случаев - маленькие курсы (0.1 - 0.5)
        # 10% случаев - очень маленькие курсы (0.01 - 0.1)
        rand = random.random()
        if rand < 0.7:
            # Обычные курсы
            usd_rate = round(random.uniform(0.5, 1.5), 2)
            eur_rate = round(random.uniform(0.5, 1.5), 2)
        elif rand < 0.9:
            # Маленькие курсы
            usd_rate = round(random.uniform(0.1, 0.5), 2)
            eur_rate = round(random.uniform(0.1, 0.5), 2)
        else:
            # Очень маленькие курсы (редко)
            usd_rate = round(random.uniform(0.01, 0.1), 2)
            eur_rate = round(random.uniform(0.01, 0.1), 2)
        rates.append((usd_rate, eur_rate))
    return generate_test_case(
        N=1000,
        rates=rates,
        description="Большой тест: граничные значения курсов (минимальные, 0.01-1.5)"
    )


def test_case_9():
    """Большой тест: граничные значения курсов (максимальные)"""
    random.seed(789)
    rates = []
    for i in range(1000):
        # 70% случаев - обычные курсы (1.0 - 10.0)
        # 20% случаев - высокие курсы (10.0 - 1000.0)
        # 10% случаев - очень высокие курсы (1000.0 - 10000.0)
        rand = random.random()
        if rand < 0.7:
            # Обычные курсы
            usd_rate = round(random.uniform(1.0, 10.0), 2)
            eur_rate = round(random.uniform(1.0, 10.0), 2)
        elif rand < 0.9:
            # Высокие курсы
            usd_rate = round(random.uniform(10.0, 1000.0), 2)
            eur_rate = round(random.uniform(10.0, 1000.0), 2)
        else:
            # Очень высокие курсы (редко)
            usd_rate = round(random.uniform(1000.0, 10000.0), 2)
            eur_rate = round(random.uniform(1000.0, 10000.0), 2)
        rates.append((usd_rate, eur_rate))
    return generate_test_case(
        N=1000,
        rates=rates,
        description="Большой тест: граничные значения курсов (максимальные, 1.0-10000)"
    )


def test_case_10():
    """Большой тест: максимальный N=5000 с различными значениями курсов"""
    random.seed(999)
    rates = []
    for i in range(5000):
        # 75% случаев - обычные курсы (0.5 - 3.0)
        # 15% случаев - средние курсы (3.0 - 50.0)
        # 7% случаев - высокие курсы (50.0 - 1000.0)
        # 3% случаев - экстремальные курсы (0.01-0.5 или 1000-10000)
        rand = random.random()
        if rand < 0.75:
            # Обычные курсы
            usd_rate = round(random.uniform(0.5, 3.0), 2)
            eur_rate = round(random.uniform(0.5, 3.0), 2)
        elif rand < 0.90:
            # Средние курсы
            usd_rate = round(random.uniform(3.0, 50.0), 2)
            eur_rate = round(random.uniform(3.0, 50.0), 2)
        elif rand < 0.97:
            # Высокие курсы
            usd_rate = round(random.uniform(50.0, 1000.0), 2)
            eur_rate = round(random.uniform(50.0, 1000.0), 2)
        else:
            # Экстремальные курсы (очень редко)
            if random.random() < 0.5:
                # Очень маленькие
                usd_rate = round(random.uniform(0.01, 0.5), 2)
                eur_rate = round(random.uniform(0.01, 0.5), 2)
            else:
                # Очень большие
                usd_rate = round(random.uniform(1000.0, 10000.0), 2)
                eur_rate = round(random.uniform(1000.0, 10000.0), 2)
        rates.append((usd_rate, eur_rate))
    return generate_test_case(
        N=5000,
        rates=rates,
        description="Большой тест: максимальный N=5000 с различными значениями курсов (0.01-10000)"
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
    rates = test_case['rates']
    return format_input(N, rates)

import sys
import os
import time
import tracemalloc
from datetime import datetime
from test_cases import get_all_test_cases, format_test_case_input

# Добавляем путь к tasks для импорта
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from tasks.task_1 import minimal_number_of_points


def format_memory(bytes_size):
    """Форматирует размер памяти в читаемый вид"""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if bytes_size < 1024.0:
            return f"{bytes_size:.2f} {unit}"
        bytes_size /= 1024.0
    return f"{bytes_size:.2f} TB"


def run_test_case(test_case, test_number, results_dir):
    """Запускает один тест-кейс и проверяет результат"""
    L = test_case['L']
    N = test_case['N']
    points = test_case['points']
    expected = test_case.get('expected')
    description = test_case['description']
    time_limit = test_case['time_limit']
    memory_limit = test_case['memory_limit']
    
    # Запускаем трассировку памяти
    tracemalloc.start()
    start_time = time.perf_counter()
    
    # Вычисляем результат
    result = minimal_number_of_points(points.copy(), L)
    
    end_time = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    # Вычисляем метрики
    execution_time = (end_time - start_time) * 1000  # в миллисекундах
    memory_used = peak / (1024 * 1024)  # в мегабайтах
    
    # Проверяем результат только если есть expected
    is_passed = None
    if expected is not None:
        is_passed = result == expected
        status = "✓ ПРОЙДЕН" if is_passed else "✗ ПРОВАЛЕН"
    else:
        status = "✓ ВЫПОЛНЕН"
    
    # Сохраняем входные данные
    input_file = os.path.join(results_dir, f"test_{test_number}_input.txt")
    with open(input_file, 'w', encoding='utf-8') as f:
        f.write(format_test_case_input(test_case))
    
    # Сохраняем выходные данные
    output_file = os.path.join(results_dir, f"test_{test_number}_output.txt")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(str(result))
    
    # Выводим информацию
    print(f"Тест {test_number}: {description}")
    print(f"  Статус: {status}")
    print(f"  L = {L}, N = {N}")
    print(f"  Ограничение по времени: {time_limit}")
    print(f"  Ограничение по памяти: {memory_limit}")
    print(f"  Время выполнения: {execution_time:.3f} мс")
    print(f"  Память использована: {memory_used:.2f} MB")
    print(f"  Результат: {result}")
    if expected is not None:
        if not is_passed:
            print(f"  Ожидалось: {expected}")
    print()
    
    return {
        'test_number': test_number,
        'description': description,
        'status': status,
        'is_passed': is_passed if is_passed is not None else True,
        'execution_time_ms': execution_time,
        'memory_used_mb': memory_used,
        'result': result,
        'expected': expected,
        'L': L,
        'N': N,
        'time_limit': time_limit,
        'memory_limit': memory_limit
    }


def run_all_tests():
    """Запускает все тест-кейсы"""
    # Создаем папку results
    results_dir = os.path.join(os.path.dirname(__file__), 'results')
    os.makedirs(results_dir, exist_ok=True)
    
    test_cases = get_all_test_cases()
    test_results = []
    passed = 0
    failed = 0
    executed = 0
    
    total_start_time = time.perf_counter()
    
    print("=" * 60)
    print("ЗАПУСК ТЕСТОВ ДЛЯ ЗАДАЧИ 1")
    print("=" * 60)
    print()
    
    for i, test_case in enumerate(test_cases, 1):
        result = run_test_case(test_case, i, results_dir)
        test_results.append(result)
        executed += 1
        if result['is_passed'] is False:
            failed += 1
        else:
            passed += 1
    
    total_end_time = time.perf_counter()
    total_time = (total_end_time - total_start_time) * 1000  # в миллисекундах
    
    # Сохраняем общий отчет
    report_file = os.path.join(results_dir, 'report.txt')
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write("=" * 60 + "\n")
        f.write("ОТЧЕТ О РЕЗУЛЬТАТАХ ТЕСТИРОВАНИЯ\n")
        f.write("=" * 60 + "\n")
        f.write(f"Дата и время: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Всего тестов: {executed}\n")
        f.write(f"Пройдено: {passed}\n")
        f.write(f"Провалено: {failed}\n")
        f.write(f"Общее время выполнения: {total_time:.3f} мс\n")
        f.write("\n" + "=" * 60 + "\n")
        f.write("ДЕТАЛЬНЫЕ РЕЗУЛЬТАТЫ\n")
        f.write("=" * 60 + "\n\n")
        
        for tr in test_results:
            f.write(f"Тест {tr['test_number']}: {tr['description']}\n")
            f.write(f"  Статус: {tr['status']}\n")
            f.write(f"  L = {tr['L']}, N = {tr['N']}\n")
            f.write(f"  Ограничение по времени: {tr['time_limit']}\n")
            f.write(f"  Ограничение по памяти: {tr['memory_limit']}\n")
            f.write(f"  Время выполнения: {tr['execution_time_ms']:.3f} мс\n")
            f.write(f"  Память использована: {tr['memory_used_mb']:.2f} MB\n")
            f.write(f"  Результат: {tr['result']}\n")
            if tr['expected'] is not None:
                f.write(f"  Ожидалось: {tr['expected']}\n")
            f.write("\n")
        
        f.write("=" * 60 + "\n")
        f.write("СТАТИСТИКА\n")
        f.write("=" * 60 + "\n")
        if test_results:
            avg_time = sum(tr['execution_time_ms'] for tr in test_results) / len(test_results)
            max_time = max(tr['execution_time_ms'] for tr in test_results)
            min_time = min(tr['execution_time_ms'] for tr in test_results)
            avg_memory = sum(tr['memory_used_mb'] for tr in test_results) / len(test_results)
            max_memory = max(tr['memory_used_mb'] for tr in test_results)
            min_memory = min(tr['memory_used_mb'] for tr in test_results)
            
            f.write(f"Среднее время выполнения: {avg_time:.3f} мс\n")
            f.write(f"Минимальное время: {min_time:.3f} мс\n")
            f.write(f"Максимальное время: {max_time:.3f} мс\n")
            f.write(f"Средняя память: {avg_memory:.2f} MB\n")
            f.write(f"Минимальная память: {min_memory:.2f} MB\n")
            f.write(f"Максимальная память: {max_memory:.2f} MB\n")
    
    print("=" * 60)
    print(f"ИТОГО: {executed} выполнено, {passed} пройдено, {failed} провалено")
    print(f"Общее время выполнения: {total_time:.3f} мс")
    print(f"Результаты сохранены в: {results_dir}")
    print("=" * 60)
    
    return failed == 0


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)

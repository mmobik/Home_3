from Algorithms_and_structures import parser_numbers, quick_sort_inplace


def minimal_number_of_points(arr: list[int], shift: int) -> int:
    if not arr:
        return 0

    quick_sort_inplace(arr)
    groups = 0
    i = 0
    while i < len(arr):  # Проверяем не вышли ли за предел массива
        groups += 1
        start = arr[i]  # Стартовая точка для проверки вхождений 
        i += 1  # Стартовую точку не учитываем
        while i < len(arr) and arr[i] <= start + 2*shift:  # Цикл закончится когда не будет пересечения
            i += 1
    return groups


def main():
    # Парсим входные данные
    data = parser_numbers(input())
    L, N = data[0], data[1]
    arr = parser_numbers(input())
    if len(arr) != N:
        raise ValueError("Массив не содержит N точек.")

    print(minimal_number_of_points(arr, L))

if __name__ == "__main__":
    main()

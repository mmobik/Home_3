def main():
    n = int(input())
    data = []
    for i in range(n):
        data.append(tuple(map(int, input().split())))  # Создаем список из кортежей
    data.sort(key=lambda x: x[1])  # Сортируем по времени окончания
    count = 0
    last_end = 0  # Последнее окончание
    for start, end in data:
        if start >= last_end + 1:  # Если начало больше или равно последнему окончанию + 1, то увеличиваем счетчик
            count += 1
            last_end = end
    print(count)



if __name__ == "__main__":
    main()

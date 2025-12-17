import sys
from Algorithms_and_structures import parser_numbers
sys.setrecursionlimit(1000000)


class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1
        return True

def main():
    # Читаем первую строку
    first_line = parser_numbers(input())
    if not first_line:
        return
    n, m = first_line[0], first_line[1]

    # Разбираем n и m
    edges = []
    for _ in range(m):
        edges.append(tuple(parser_numbers(input())))
    
    # Проверка на несвязность при отсутствии ребер
    if m == 0 and n > 1:
        print("Oops! I did it again")
        return
    
    # Сортировка по убыванию веса для максимального остовного дерева
    edges.sort(key=lambda x: x[2], reverse=True)
    
    # Инициализация DSU
    dsu = DSU(n)
    total_weight = 0
    edges_used = 0
    
    # Основной алгоритм Крускала
    for u, v, w in edges:
        if dsu.union(u, v):  # если ребро не создает цикл
            total_weight += w
            edges_used += 1
            if edges_used == n - 1:  # набрали достаточно ребер
                break
    
    # Проверка связности графа
    # Если все вершины в одном множестве - граф связный
    root = dsu.find(1)
    for i in range(2, n + 1):
        if dsu.find(i) != root:
            print("Oops! I did it again")
            return
    
    print(total_weight)

if __name__ == "__main__":
    main()

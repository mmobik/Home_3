import sys

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
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

def solve():
    # Читаем n и k
    n, k = map(int, input().split())
    
    # Читаем города с электростанциями (переводим в 0-based)
    stations = list(map(int, input().split()))
    stations = [x - 1 for x in stations]
    
    # Создаём список рёбер
    edges = []
    
    # Добавляем фиктивные рёбра от источника к электростанциям
    source = n  # фиктивный источник
    for station in stations:
        edges.append((0, source, station))
    
    # Читаем матрицу стоимостей и добавляем рёбра между городами
    for i in range(n):
        row = list(map(int, input().split()))
        for j in range(i + 1, n):  # только верхний треугольник
            edges.append((row[j], i, j))
    
    # Сортируем рёбра по стоимости
    edges.sort()
    
    # Инициализируем DSU для n+1 вершин
    dsu = DSU(n + 1)
    
    total_cost = 0
    edges_used = 0
    target_edges = n  # для (n+1) вершин нужно n рёбер в MST
    
    # Алгоритм Крускала
    for cost, u, v in edges:
        if dsu.union(u, v):
            total_cost += cost
            edges_used += 1
            if edges_used == target_edges:
                break
    
    print(total_cost)

if __name__ == "__main__":
    solve()

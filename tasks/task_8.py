import math

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))  # БЕЗ +1, т.к. индексы 0..n-1
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

def main():
    n = int(input())
    towers = []
    
    # Читаем координаты вышек
    for _ in range(n):
        x, y = map(int, input().split())
        towers.append((x, y))
    
    # Создаём список всех рёбер: (расстояние, i, j)
    edges = []
    for i in range(n):
        xi, yi = towers[i]
        for j in range(i + 1, n):
            xj, yj = towers[j]
            dist = math.sqrt((xj - xi)**2 + (yj - yi)**2)
            edges.append((dist, i, j))
    
    # Сортируем рёбра по расстоянию (по возрастанию для MST)
    edges.sort()
    
    # Инициализируем DSU
    dsu = DSU(n)
    total_edges_used = 0
    max_edge_in_mst = 0
    
    # Алгоритм Крускала для MST
    for dist, u, v in edges:
        if dsu.union(u, v):
            max_edge_in_mst = max(max_edge_in_mst, dist)
            total_edges_used += 1
            if total_edges_used == n - 1:  # построили MST
                break
    
    # Выводим ответ с точностью до 4 знаков
    print(f"{max_edge_in_mst:.4f}")

if __name__ == "__main__":
    main()

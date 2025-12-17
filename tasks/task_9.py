import math

def solve():
    N, M = map(int, input().split())
    K = int(input())
    
    # Создаём множество диагональных кварталов для быстрой проверки
    diagonal = set()
    for _ in range(K):
        x, y = map(int, input().split())
        diagonal.add((x, y))
    
    # Инициализация DP массива
    INF = float('inf')
    dp = [[INF] * (M + 1) for _ in range(N + 1)]
    dp[0][0] = 0
    
    # Диагональная стоимость
    DIAG_COST = 100 * math.sqrt(2)
    
    for i in range(N + 1):
        for j in range(M + 1):
            # С востока
            if i > 0:
                dp[i][j] = min(dp[i][j], dp[i-1][j] + 100)
            # С юга
            if j > 0:
                dp[i][j] = min(dp[i][j], dp[i][j-1] + 100)
            # С юго-запада (диагональ)
            if i > 0 and j > 0:
                if (i, j) in diagonal:  # Квартал (i,j) можно пройти по диагонали
                    dp[i][j] = min(dp[i][j], dp[i-1][j-1] + DIAG_COST)
                else:
                    dp[i][j] = min(dp[i][j], dp[i-1][j-1] + 200)  # Обход по сторонам
    
    # Округление до целых метров
    result = round(dp[N][M])
    print(result)

if __name__ == "__main__":
    solve()

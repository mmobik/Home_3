def solve():
    N = int(input())
    K = int(input())
    
    if N == 1:
        print(K - 1)
        return
    
    dp0 = 0  # Количество способов получить последовательность где последнее число 0
    dp1 = K - 1  # Количество способов получить последовательность где последнее число не 0
    
    for i in range(2, N + 1):
        new_dp0 = dp1
        new_dp1 = (dp0 + dp1) * (K - 1)
        dp0, dp1 = new_dp0, new_dp1
    
    print(dp0 + dp1)

if __name__ == "__main__":
    solve()

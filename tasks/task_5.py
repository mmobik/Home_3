def lucky_tickets(N, M):
    K = N // 2
    max_sum = K * (M - 1)
    
    dp_prev = [0] * (max_sum + 1)
    dp_prev[0] = 1
    
    for length in range(1, K + 1):
        dp_curr = [0] * (max_sum + 1)
        for s in range(max_sum + 1):
            for digit in range(M):
                if s >= digit:
                    dp_curr[s] += dp_prev[s - digit]
        dp_prev = dp_curr
    
    total = 0
    for s in range(max_sum + 1):
        total += dp_prev[s] * dp_prev[s]
    
    return total

def main():
    N, M = map(int, input().split())
    print(lucky_tickets(N, M))

if __name__ == "__main__":
    main()

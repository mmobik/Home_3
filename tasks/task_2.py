def solve():
    n = int(input())
    rub, usd, eur = 100.0, 0.0, 0.0  # начальные состояния
    
    for _ in range(n):
          # курс доллара и евро
        a, b = map(float, input().split())  # курс доллара и евро
        # Пересчитываем состояния на конец текущего дня
        new_rub = max(rub, usd * a, eur * b)
        new_usd = max(usd, rub / a, eur * b / a)
        new_eur = max(eur, rub / b, usd * a / b)
        
        rub, usd, eur = new_rub, new_usd, new_eur
    
    print(f"{rub:.2f}")  # ответ - максимальные рубли в конце



if __name__ == "__main__":
    solve()

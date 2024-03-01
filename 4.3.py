X, Y, N = map(int, input().split())
Rubles = (X * N) + (Y * N) // 100
Kopeck = (Y * N) % 100
print(Rubles,'руб.', Kopeck,'коп.')

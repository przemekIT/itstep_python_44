# Wydrukuj romb złożony z gwiazdek.

n = int(input("Podaj wysokość połowy rombu (liczba wierszy): "))

# Górna połowa rombu
for i in range(1, n+1):
    print(" " * (n - i) + "*" * (2 * i - 1))

for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))



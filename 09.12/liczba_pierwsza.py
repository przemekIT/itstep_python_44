N = int(input("Podaj liczbę całkowitą większą od 2: "))

if N > 2:
    print(f"Liczby pierwsze mniejsze niż {N}")
    for num in range(2, N):
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num, end = " ")
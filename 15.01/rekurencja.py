# silnia
# 7! = 6! * 7
# 6! = 5! * 6
# 5! = 4! * 5
# 4! = 3! * 4
# 3! = 2! * 3
# 2! = 1! * 2
# 1! = 1 
# 0 

# Kluczowe elementy: warunek brzegowy, podproblem, rozwiązanie globalne
def silnia(n):
    if n == 0: # warunek brzegowy
        return 1
    return n * silnia(n-1) # wywołanie rekurencyjne

print(silnia(7))
print(7*6*5*4*3*2*1)

# Stwórz funkcję rekurencyjną obliczającą ciąg fibonacciego
# fibonacci(5) => 2 + 3 = 5
# fibonacci(8) => 8 + 13 = 21

# fibonacci(5) => fibonacci(3) + fibonacci(4)
# fibonacci(4) => fibonacci(2) + fibonacci(3)
# fibonacci(3) => fibonacci(1) + fibonacci(2)
# fibonacci(2) => fibonacci(0) + fibonacci(1)
# fibonacci(0) => 0 warunek brzegowy
# fibonacci(1) => 1 warunek brzegowy

def fibonacci(n):
    if n < 0:
        return "Podaj wartość większą od 0!"
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2) # wywołanie rekurencyjne

print(fibonacci(11))


def generuj_listę(n, wynik = []):
    if n == 0:
        return wynik
    wynik.append(n)
    return generuj_listę(n-1, wynik)

print(generuj_listę(3))



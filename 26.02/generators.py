# Tworzymy generator
def licznik():
    print("Start generator")
    yield {"key1": 1}
    yield {"key2": 2}
    yield {"key3": 3}

lst = [1,2,3]


gen = licznik()
print(gen)
print(next(gen))
print(next(gen))

# for i in gen:
#     print(i)

# # Każdy generator jest iteratorem, natomiast nie każdy iterator jest generatorem.
# gen = (x**2 for x in range(5))

# print(type(gen))
# print(next(gen))
# print(next(gen))

# lista = [1,2,3,4,5]
# it = iter(lista)

# for i in it:
#     print(i)


# # lista = [1,2,3,4....] # Tworzenie listy zawierających 100 elementów w bazie i zajmowanie pamięci => Nieefektywne

# # Stworzenie generatora dla generowania 100 elementów z bazy => Efektywne
# def pobierz_dane_baza():
#     for i in range(1, 101): # Symulujemy 100 rekordów w bazie
#         yield f"Rekord {i}"

# gen = pobierz_dane_baza()

# for _ in range(50):
#     print(next(gen))



# import time

# # Złożoność obliczeniowa O(n^2)
# def fibonacci_rekurencja(n):
#     if n== 0:
#         return 0
#     elif n == 1:
#         return 1
#     return fibonacci_rekurencja(n-1) + fibonacci_rekurencja(n-2)

# start = time.time()
# fibb10 = fibonacci_rekurencja(40) 
# end = time.time()
# print(f"Złożoność rekurencyjna dla n={40}: Czas: {end-start:.16f} sekundy")

# # Złożoność obliczeniowa O(n)
# def fibonacci_generator():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b

# gen = fibonacci_generator()

# start = time.time()
# for i in range(41):
#     print(next(gen), end = " ")
# end = time.time()
# print(f"Złożoność generatora dla n={40}: Czas: {end-start:.16f} sekundy")


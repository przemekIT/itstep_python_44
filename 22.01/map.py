# # Funkcja map
# # map(function, iterable_object)

# # Przykład 1: PRosta transformacja
# numbers = [1,2,3,4,5]
# result = map(lambda x: x+1, numbers)

# print(list(result))

# # Przykład 2: Konwersja typów
# str_numbers = ["1", "2", "3", "4"]
# result = map(int, str_numbers)

# print(list(result))

# # Przykład 3: Operacja na dwóch listach
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]

# result = map(lambda x, y: x + y, list1, list2)

# print(list(result))

# # Przykład 4: Modyfikacja tekstu
# words = ["python", "map", "function"]

# result = map(str.upper, words)

# print(list(result))

# Zadanie: Mamy listę uczniów, gdzie każdy element jest listą zawierającą 
# imię ucznia i listę jego ocen z różnych przedmiotów.
# 1. Obliczyć średnią ocen dla każdego ucznia
# 2. Zwrócić listę list, gdzie każda lista zawiera imię ucznia i jego 
#    średnią ocenę.
# 3. Wynik zaokrąglić do dwóch miejsc po przecinku.

# Wymaganie: wykorzystaj funkcję map() do obliczenia wyników

students = [
    ["Jan", [5,4,3,5]],
    ["Anna", [3,5,4,4,5]],
    ["Piotr", [2,3,3,4]],
    ["Maria", [6,5,5,6,5]]
]

# wynik: [["Piotr", 4.25], ["Anna", 4.2] ...]

def calculate_average(student):
   name, grades = student
   average = sum(grades) / len(grades)
   return [name, f"{average:.2f}"]

result = list(map(calculate_average, students))

print(result)

sorted_list = sorted(result, key = lambda x: x[1], reverse=True)
print(sorted_list)


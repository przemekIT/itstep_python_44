from functools import reduce

oceny = [
    [80, 90, 78, 92, 88], # student 1
    [45, 60, 55, 70, 65], # student 2
    [95, 85, 100, 90, 98], # student 3
    [30, 40, 35, 50, 45], # student 4
    [70, 75, 80, 85, 90] # student 5
]

# 1 - Obliczanie średniej ocen dla każdego studenta
srednie_oceny = list(map(lambda oceny_studenta: reduce(lambda x, y: x + y, oceny_studenta)/len(oceny_studenta), oceny))
print(srednie_oceny)

# 2 - Znajdz studentów, którzy zdali egzamin 
zdali = list(filter(lambda srednia: srednia >= 50, srednie_oceny))

# 3 - Znalezienie studenta z najwyższą średnią ocen (reduce)
najlepszy_student_index = reduce(lambda acc, i: i if srednie_oceny[i] > srednie_oceny[acc] else acc, range(len(srednie_oceny)))

# 4 - Konwersja ocen na skale A-F (map)
def ocena_na_skale(ocena):
    if 90 <= ocena <= 100:
        return 'A'
    elif 80 <= ocena < 90:
        return 'B'
    elif 70 <= ocena < 80:
        return 'C'
    elif 60 <= ocena < 70:
        return 'D'
    elif 50 <= ocena < 60:
        return 'E'
    else:
        return 'F'
    
oceny_literowe = list(map(lambda oceny_studenta: list(map(ocena_na_skale, oceny_studenta)), oceny))

# 5 - Oblicz średnią ocen z każdego przedmiotu
# oceny = [
#     [4,5,3], # 1 uczeń (Matematyka, Angielski, Polski)
#     [3,4,2], # 2 uczeń (Matematyka, Angielski, Polski)
#     [5,3,4] # 3 uczeń (Matematyka, Angielski, Polski)
# ]

# print(list(zip(oceny))) # => 
# # [   (4, 3, 5), # Matematyka (1 uczeń, 2 uczeń, 3 uczeń)
# #     (5, 4, 3), # Angielski (1 uczeń, 2 uczeń, 3 uczeń)
# #     (3, 2, 4) # Polski (1 uczeń, 2 uczeń, 3 uczeń)
# # ]

# 6 - Oblicz średnią ocen z każdego przedmiotu
srednie_przedmioty = list(map(lambda przedmiot: reduce(lambda x, y: x + y, przedmiot)/len(przedmiot), zip(*oceny)))

# Wyniki
print(f"Średnie oceny studentów: {srednie_oceny}")
print(f"Studenci, którzy zdali (średnia >= 50): {zdali}")
print(f"Najlepszy student: Student {najlepszy_student_index + 1} (średnia: {srednie_oceny[najlepszy_student_index]})")
print(f"Oceny w skali A-F dla każdego studenta: ")
for i, oceny_studenta in enumerate(oceny_literowe):
    print(f"Student {i+1}: {oceny_studenta}")
print(f"Średnie oceny z przedmiotów: {srednie_przedmioty}")

 



import random

# funkcja rekurencyjna
def find_min_sum_recursive(lst, start=0, min_sum=float('inf'), min_index=0):
    # Warunek końca rekurencji - jeśli pozostałe elementy < 10
    if start > len(lst) - 10:
        return min_index
    
    # Obliczamy sumę dla bieżacego ciągu 10 elementów
    current_sum = sum(lst[start:start + 10])

    # Jeśli bieżąca suma jest mniejsza niż aktualna najmniejsza suma
    if current_sum < min_sum:
        min_sum = current_sum
        min_index = start

    # Rekurencyjne wywołanie dla następnego indeksu
    return find_min_sum_recursive(lst, start+1, min_sum, min_index)

random_numbers = [14, 76, 15, 100, 93, 53, 31, 38, 44, 10, 4, 24, 86, 31, 51, 6, 83, 97, 98, 96, 11, 18, 66, 92, 0, 48, 24, 23, 7, 15, 97, 79, 12, 8, 63, 65, 85, 84, 79, 6, 8, 87, 4, 54, 20, 62, 44, 61, 78, 93, 44, 20, 22, 23, 57, 85, 66, 75, 68, 39, 71, 34, 76, 86, 97, 47, 19, 38, 13, 34, 98, 19, 4, 4, 90, 77, 77, 47, 81, 24, 51, 60, 82, 83, 17, 53, 60, 70, 24, 90, 80, 7, 18, 55, 83, 19, 64, 98, 84, 10]


min_index = find_min_sum_recursive(random_numbers)

print("Lista liczb:", random_numbers)
print("Indeks początkowy ciągu o najmniejszej sumie:", min_index)
print("Ciąg: ", random_numbers[min_index:min_index+10])
print("Suma tego ciągu:", sum(random_numbers[min_index:min_index+10]))



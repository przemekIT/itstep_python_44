import random   
from functools import reduce

# Generowanie losowej lsity liczb całkowitych
data = [random.randint(-5,5) for _ in range(9)]

# Zadanie 1
# Suma liczb ujemnych
sum_negative = sum(x for x in data if x < 0)

# Suma liczb parzystych
sum_even = sum(x for x in data if x % 2 == 0)

# Suma liczb nieparzystych
sum_odd = sum(x for x in data if x % 2 != 0)

# Iloczyn elementów o indeksach podzielnych przez 3
product_indices_div3 = 1
for i in range(len(data)):
    if i % 3 == 0 and i != 0:
        product_indices_div3 *= data[i]

# Iloczyn elementów pomiędzy najmniejszym i największym elementem;
min_val, max_val = min(data), max(data)
min_idx, max_idx = data.index(min_val), data.index(max_val)
if min_idx > max_idx:
    min_idx, max_idx = max_idx, min_idx
product_between_min_max = 1
if max_idx - min_idx > 1:
    for x in data[min_idx+1: max_idx]:
        product_between_min_max *= x

# Suma elementów pomiędzy pierwszym i ostatnim elementem dodatnim
positive_indices = [i for i,x in enumerate(data) if x > 0]
if len(positive_indices) >= 2:
    sum_between_first_last_positive = sum(data[positive_indices[0] + 1: positive_indices[-1]])
else:
    sum_between_first_last_positive = 0

print("Lista danych: ", data)
print("Suma liczb ujemnych: ", sum_negative)
print("Suma liczb parzystych: ", sum_even)
print("Suma liczb nieparzystych: ", sum_odd)
print("Iloczyn elementów o indeksach podzielnych przez 3: ", product_indices_div3)
print("Iloczyn elementów pomiędzy najmniejszym i największym elementem: ", product_between_min_max)
print("Suma elementów pomiędzy pierwszym i ostatnim elementem dodatnim: ", sum_between_first_last_positive)


# Zadanie 2
even_numbers =[x for x in data if x % 2 == 0]

odd_numbers = [x for x in data if x % 2 != 0]

negative_numbers = [x for x in data if x < 0]

positive_numbers = [x for x in data if x > 0]



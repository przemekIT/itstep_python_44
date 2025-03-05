x = 2

y = 3

str = "Hello"

lst = [x, x, y, str]

print(lst)
print(lst[0])
print(lst[-1])
print(lst[1:1])
print(lst[::-1])

# 1. Listy w pythonie są MUTOWALNE
# 2. Listy Pythonie są POSORTOWANE
# 3. Indeksowalne, czyli mozemy uzyskać elementy za pomocą INDEKSÓW
# 4. Mogą zawierać elementy, o róznych typach
# 5. Elementy mogą się powtarzać

# print(id(lst))
# lst[0] = 5
# print(id(lst))


# str = "Hello"
# print(id(str))
# str = "Nowe hello"
# print(id(str))

# print(lst)
str = "Hello"
print(id(str))
print(id(str.replace(str, "newhello")))



lst = [1,2, [3,4, [4,5, [6,7]]]]
print(lst[-1][-1][-1][-1])


# append
new_list = [1,2,3,4,3,3]
# new_list.append()
print(new_list)

# insert
new_list.insert(1, [10,123])
print(new_list)

# extend - rozszerza listę o elementy innej listy
new_list.extend([10,11,12])
print(new_list)

# USUWANIA ELEMENTÓW Z LISTY
new_list.remove(3)
print(new_list)



## zadanie 1
# a = int(input("Podaj pierwszą liczbę: "))
# b = int(input("Podaj drugą liczbę: "))

# print("Liczby z podanego zakresu: ")

# for i in range(a, b+1):
#     print(i)


# # zadanie 2
# a = int(input("Podaj pierwszą liczbę: "))
# b = int(input("Podaj drugą liczbę: "))

# print("Liczby nieparzyste z podanego zakresu: ")

# for i in range(a, b+1):
#     if i % 2 != 0:
#         print(i)

# # zadanie 3
# a = int(input("Podaj pierwszą liczbę: "))
# b = int(input("Podaj drugą liczbę: "))

# print("Liczby parzyste z podanego zakresu: ")

# for i in range(a, b+1):
#     if i % 2 == 0:
#         print(i)

# zadanie 4
# a = int(input("Podaj pierwszą liczbę: "))
# b = int(input("Podaj drugą liczbę: "))

# print("Liczby z podanego zakresu w kolejności malejącej: ")

# for i in range(max(a, b), min(a, b) - 1, -1):
#     print(i)


# zadanie 5
a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))

print("Liczby nieparzyste z podanego zakresu po normalizacji: ")

for i in range(min(a,b), max(a, b) + 1):
    if i % 2 != 0:
        print(i)
        print(i+1)




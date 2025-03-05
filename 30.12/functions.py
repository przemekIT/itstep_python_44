# def printMsg2(myMsg1 = "Default", myMsg2 = "Deefault2"):
#     print(myMsg1)
#     print(myMsg2)

# x = "Hello"
# y = "World"

# printMsg2(x)


# def modifyName(userName):
#     newName = userName.upper()
#     return newName

# name = input("Input your name:")
# newName = modifyName(name)
# print(newName)

# def powitanie(imie="Gość"):
#     print(f"Witaj {imie}")
#     return f"Witaj, {imie}!"

# print(powitanie("Przemek"))

# def suma(*liczby):
#     '''Sumuje dowolną liczbę argumentów.'''
#     return sum(liczby)

x  = 10 # zmienna globalna

# def my_local_function():
#     x = 5 # zmienna lokalna
#     print("Wartość x: ", x)

# my_local_function()
# print("Wartość druga x: ", x)


# lambda argumenty: wyrażenie (ciało funkcji)

kwadrat = lambda x: x ** 2
suma = lambda a,b: a+b
parzysta = lambda x: "Tak" if x % 2 == 0 else "Nie"

osoby = [("Jan", 25, 200), ("Anna", 30, 150), ("Piotr", 20, 180)]

posortowane = sorted(osoby, key = lambda x: x[1])
print(posortowane)
posortowane_wzrost = sorted(osoby, key = lambda x: x[2])
print(posortowane_wzrost)

# print(kwadrat(5))
# print(suma(3,7))
# print(parzysta(4))
# print(parzysta(5))

# x  = 10 # zmienna globalna

# def my_local_function():
#     x = 5 # zmienna lokalna
#     print("Wartość x: ", x)

# my_local_function()
# print("Wartość druga x: ", x)

# modyfikowanie zmiennej globalnej w funkcji

# x  = 10 # zmienna globalna

# def zmien_globalna():
#     global x
#     x = 5 # zmienna lokalna
#     print("Wartość x: ", x)

# zmien_globalna()
# print("Wartość druga x: ", x)

def funkcja_otaczajaca():
    x = 20
    print(id(x))
    def funkcja_wewnetrzna():
        nonlocal x
        x=30
        print(id(x))
        x += 5
        print("Otaczająca zmienna x: ", x)
    print(x)
    funkcja_wewnetrzna()

funkcja_otaczajaca()


def logger(funkcja):
    def wrapper(*args, **kwargs): # Przechwycenie dowolnych argumentów
        print(f"Wywołano {funkcja.__name__} z argumentami {args} {kwargs}")
        return funkcja(*args, **kwargs) # Przekazanie argumentów do oryginalnej funkcji
    return wrapper

@logger
def suma(key1, key2):
    return key1 + key2

@logger
def multiply(key1, key2):
    return key1*key2

print(suma(key1 = 4, key2 = 5))
print(multiply(key1 = 4, key2 = 5))


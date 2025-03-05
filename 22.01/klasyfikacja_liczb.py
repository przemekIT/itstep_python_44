numbers = [4, -3, 0, 7, -8, -1, 10]

# Funkcja klasyfikująca liczby
def classify_number(num):
    if num == 0:
        return [num, "zero"]
    elif num > 0 and num % 2 == 0:
        return [num, "even-positive"]
    elif num < 0 and num % 2 == 0:
        return [num, "even-negative"]
    elif num > 0 and num % 2 != 0:
        return [num, "odd-positive"]
    else:
        return [num, "odd-negative"]
    
result = list(map(classify_number, numbers))

print(result)

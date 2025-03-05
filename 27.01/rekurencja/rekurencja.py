# Warunek bazowy (base case) - najprostszy przypadek problemu, ktory mozna rozwiązać bez dalszych wywołań rekurencyjnych. 
# Jest konieczny, aby rekurencja zakończyła się.

# Wywołanie rekurencyjne (recursive call) - funkcja wywołuje samą siebie, rozwiązując mniejszą część problemu.


# Silnia n!, to iloczyn wszystkich liczb od 1 do n, n! = n * (n-1)!, (n-1)! = n * (n-1)(n-2)!
# 5**4 => 5 * 5**3 => 5 * 5 * 5**2 => 5*5*5*5

def factorial(n):
    if n == 0: # Warunek bazowy
        return 1
    else:
        print(n)
        return n*factorial(n-1) # Wywołanie rekurencyjne
    

print(factorial(5)) #120

# factorial(5) => return (5 * factorial(4))
# factorial(4) => return (4 * factorial(3))
# factorial(3) => return (3 * factorial(2))
# factorial(2) => return (2 * factorial(1))
# factorial(1) => return (1 * factorial(0))
# factorial(0) => return 1

# Ciąg fibonnaci

def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    


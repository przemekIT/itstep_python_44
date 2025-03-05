# Funkcja filter

# filter(function, iterable_object)

# Przykład 1: Filtrowanie liczb parzystycch
numbers = [1,2,3,4,5,6]
result = filter(lambda x: x % 2 == 0, numbers)

print(list(result))

# Przykład 2: Filtrowanie ciągów znaków o określonej długości
words = ["cat", "dog", "elephant", "bat"]
result = filter(lambda word: len(word) > 3, words)

print(list(result))

# Przykład 3: Usuwanie wartości pustych
data = [0, 1, '', 'hello', [], [1,2], None]
result = filter(bool, data)

print(list(result))

# Przykład 4: Filtrowanie elementów na podstawie własnej funkcji

characters = ['a', 'b', 'c', 'f', 'o', 'e']
# chcemy wyfiltrować wszystkie litery, które należą do a,e,i,o,u

def is_vowel(char):
    return char.lower() in 'aeiou'

result = filter(is_vowel, characters)
print(list(result))


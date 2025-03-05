# lambda arugments: expression

# Przykład 1
add = lambda x,y: x+y

def add2(x,y):
    return x +y

# add = add2

result = add(5,10)
result2 = add2(5,10)

print(result2)
print(result)

# Przykład 2
square = lambda x: x ** 2
print(square(4))

# Przykład 3
# sorted(iterable_object, key = lambda x: expression, reverse = True)

people = ["Anna", "Bartosz", "daria", "Cesław"]

sorted_people = sorted(people, key = lambda person: person.lower())

print(sorted_people)


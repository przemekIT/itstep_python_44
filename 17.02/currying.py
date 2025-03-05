from functools import partial

def add(x, y):
    return x + y

add_10 = partial(add, 10)

numbers = [1,2,3,4,5]

new_numbers = list(map(add_10, numbers))

print(new_numbers)


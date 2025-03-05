def all_positive(sublist):
    return all(num>0 for num in sublist)


#[True, True, True]
#[False, True, True]


matrix = [
    [1, 2, 3],
    [-1, 4, 5],
    [6, 7, 8],
    [9, -10, 11],
    [12, 13, 14]
]

result = filter(all_positive, matrix)
print(list(result))
import copy

A = [1,2,3,[4,5]]

B = copy.deepcopy(A)
print(B)
B[3][0] = 99
print(B)
print(A)
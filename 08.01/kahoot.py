# lst = []
# for i in range(5):
#     for j in range(2):
#             # i = 0 j = 0
#             # i = 0 j = 1
#             # i = 1 j = 0
#             # i = 1 j = 1
#             lst.append(i)

# print(lst)

# lst = [1,2,3]

# nested = []

# for i in lst:
#     lst2 = []
#     for j in lst:
#         lst2.append(i+j)
#     nested.append(lst2)

# print(nested)

# nested2 = [[x+y for y in lst] for x in lst]
# print(nested2)

# 


# print(flattened[:4])

data = [2,4,6,8]

result = [x * y for x in data for y in data if x != y and x * y % 4 == 0]
print(result)
print(result[-3:])
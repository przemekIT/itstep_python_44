import re

pattern = r"\s+"
text = "Ala ma kota"
matches = re.split(pattern, text)
print(matches)

# userStr = "abcd abc efgh"
# match = re.search(r'\w{4}', userStr)
# print(match)

# str = "helloworld"

# print(str.lower())
# print(str.upper())
# print(str.capitalize())
# print(str.title())
# print(str.swapcase())

# print(str.find("world")) 
# print(str.find("przemek"))
# print(str.index("world"))
# print(str.count("world"))
# print(str.count("o"))
# print(str.startswith("hell2o"))
# print(str.endswith("world"))
# print(str.isalpha())
# print(str.isdigit())
# print(str.isalnum())
# print(str.isspace())
# print(str.strip())
# str2 = str.replace("helloworld", "newstring").strip()
# print(str2)
# print(str[-1])
# print(str[:-1])
# str2 = r"Hello\UWorld!"
# print(str2)

import re

text = "Urodziłem się 15-08-1990 , a mój brat 01-01-1985."

pattern = r"\b\d{2}-\d{2}-\d{4}\b"

dates = re.findall(pattern, text)
print(dates)









# pattern = r"<[^>]+>"

# # Znajdź wszystkie tagi html
# tags = re.findall(pattern, text)
# print(tags)





# # Sprawdź czy tekst jest adresem e-mail

# pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
# #test, user.name123, abc_def%+

# is_email = bool(re.match(pattern, text))

# is_eu = bool(re.match(pattern,text))

# if is_eu:
#     print("Domena jest eu!")
# else:
#     print("Domena nie jest eu!")

# print(is_email)
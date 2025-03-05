text ='Aą'
encoded = text.encode('utf-8') # zapisuje tekst jako bajty w utf 8
print(encoded)

# Odczyt bajtów z utf-8
decoded = encoded.decode('utf-8') #odtwarza tekst
print(decoded)
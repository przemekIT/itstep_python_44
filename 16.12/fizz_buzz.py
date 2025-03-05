start = int(input("Podaj punkt początkowy zakresu: "))
end = int(input("Podaj punkt końcowy zakresu: "))

wynik = ["Fizz Buzz" if liczba % 3 == 0 and liczba % 5 == 0 and liczba != 0
         else "Fizz" if liczba % 3 == 0 and liczba != 0
         else "Buzz" if liczba % 5 == 0 and liczba != 0
         else liczba 
         for liczba in range(start, end + 1)]

print(wynik)

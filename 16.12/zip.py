list1 = [1,2,3,4,5]
list2 = [1, 2, "Fizz", 4, "Fizz"]

wynik = [fizz if isinstance(fizz, int) else str(x) + " " + fizz for x, fizz in zip(list1, list2)]

print(wynik)

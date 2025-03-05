długość = int(input("Podaj długość prostokąta: "))
szerokość = int(input("Podaj szerokość prostokąta: "))

for i in range(długość):
    if i == 0 or i == długość - 1:
        print("*" * szerokość)
    else:
        print("*" + " " * (szerokość -2) + "*")


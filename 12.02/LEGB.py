# zmienna w zakresie globalnym
x = "global"

def outer_function():
    # zmienna w zakresie zamykającym (enclosing)
    x = "enclosing"

    def inner_function():
        x = "local"
        # zmienna w zakresie lokalnym
        print("Wewnątrz inner_function: ", x)

    inner_function()

    print("Wewnątrz funkcji outer_function: ", x)

outer_function()
print("Na poziomie globalnym: ", x)
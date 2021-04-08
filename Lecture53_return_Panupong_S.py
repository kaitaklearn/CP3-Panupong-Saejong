priceInput = int(input("Price : "))
def vat7(priceInput):
    result = priceInput+(priceInput * 7 / 100)
    return result
print(vat7(priceInput))
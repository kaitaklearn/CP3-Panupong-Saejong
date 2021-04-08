def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        return (showMenu())
    else:
        print("User or Password Wrong.")
        return login()
def showMenu():
    print("---Please Choose Menu---")
    print("1. Vat7")
    print("2. Calculation")
    print("3. Vat Calulation")
    return menuSelect()
def menuSelect():
    usernameSelect1 = int(input("เลือกเมนู "))
    if usernameSelect1 == 1:
        price = int(input("Price : "))
        vat = 7
        result = price + (price * vat / 100)
        print("ราคารวม Vat7 %",result)
        return menuSelect()
    elif usernameSelect1 == 2:
        price1 = int(input("ราคาชิ้นที่ 1 : "))
        price2 = int(input("ราคาชิ้นที่ 2 : "))
        sum = price1 + price2
        print("ราคารวม :",sum)
        return menuSelect()
    elif usernameSelect1 == 3:
        return (priceResult())
def vat7(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return result
def priceResult():
    price1 = int(input("ราคาชิ้นที่ 1 : "))
    price2 = int(input("ราคาชิ้นที่ 2 : "))
    return vat7(price1+price2)
print(login())

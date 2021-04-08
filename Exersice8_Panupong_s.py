coke = 15
pepsi = 15
orange_juice = 25
coconut = 35
coffee = 50
usernameInput = input("Username : ")
passwordInput = input("Password : ")
if usernameInput == "kaitak" and passwordInput == "kaitakshop":
    print("Welcome to Kaitak Shop")
    print("---Please Choose Menu---")
    print("1. Coke         ", "Price", coke, "THB")
    print("2. Pepsi        ", "Price", pepsi, "THB")
    print("3. Orange_Juice ", "Price", orange_juice, "THB")
    print("4. Coconut      ", "Price", coconut, "THB")
    print("5. Coffee       ", "Price", coffee, "THB")
    usernameSelect1 = int(input("เลือกสินค้า (1-5) "))
    qrt = int(input("ใส่จำนวน : "))
    if usernameSelect1 == 1:
        price = qrt * coke
        print("Coke","จำนวน",qrt,"ราคา", price, "THB")
    elif usernameSelect1 == 2:
        price = qrt * pepsi
        print("Pepsi","จำนวน",qrt,"ราคา", price, "THB")
    elif usernameSelect1 == 3:
        price = qrt * orange_juice
        print("Orange_Juice","จำนวน",qrt,"ราคา", price, "THB")
    elif usernameSelect1 == 4:
        price = qrt * coconut
        print("Coconut","จำนวน",qrt,"ราคา", price, "THB")
    elif usernameSelect1 == 5:
        price = qrt * coffee
        print("Coffe","จำนวน",qrt,"ราคา", price, "THB")
    usernameSelect2 = int(input("เลือกสินค้า (1-5) "))
    qrt2 = int(input("ใส่จำนวน : "))
    if usernameSelect2 == 1:
        price2 = qrt2 * coke
        print("Coke","จำนวน",qrt2,"ราคา", price2, "THB")
    elif usernameSelect2 == 2:
        price2 = qrt2 * pepsi
        print("Pepsi","จำนวน",qrt2,"ราคา", price2, "THB")
    elif usernameSelect2 == 3:
        price2 = qrt2 * orange_juice
        print("Orange_Juice","จำนวน",qrt2,"ราคา", price2, "THB")
    elif usernameSelect2 == 4:
        price2 = qrt2 * coconut
        print("Coconut","จำนวน",qrt2,"ราคา", price2, "THB")
    elif usernameSelect2 == 5:
        price2 = qrt2 * coffee
        print("Coffe","จำนวน",qrt2,"ราคา", price2, "THB")
    usernameSelect3 = int(input("เลือกสินค้า (1-5) "))
    qrt3 = int(input("ใส่จำนวน : "))
    if usernameSelect3 == 1:
        price3 = qrt3 * coke
        print("Coke", "จำนวน", qrt3, "ราคา", price3, "THB")
    elif usernameSelect3 == 2:
        price3 = qrt3 * pepsi
        print("Pepsi", "จำนวน", qrt3, "ราคา", price3, "THB")
    elif usernameSelect3 == 3:
        price3 = qrt3 * orange_juice
        print("Orange_Juice", "จำนวน", qrt3, "ราคา", price3, "THB")
    elif usernameSelect3 == 4:
        price3 = qrt3 * coconut
        print("Coconut", "จำนวน", qrt3, "ราคา", price3, "THB")
    elif usernameSelect3 == 5:
        price3 = qrt3 * coffee
        print("Coffe", "จำนวน", qrt3, "ราคา", price3, "THB")
    print("ราคารวมทั้งหมด",price+price2+price3,"THB")
    print("ขอขอบคุณที่ใช้บริการ Kaitak Shop")
else:
    print("Username/Password ผิดพลาดลองใหม่อีกครั้ง")
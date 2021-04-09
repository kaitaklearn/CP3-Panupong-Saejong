menu = {"ข้าวมันไก่":45,"ข้าวหน้าเป็ด":50,"ข้าวขาหมู":50,"กระเพราไข่ดาว":50}
menuList = []

def showBill():
    result = 0
    print("---- My Food ----")
    for number in range(len(menuList)):
        result += int(menuList[number][1])
        print(menuList[number][0],menuList[number][1])
    print("Total :",result)


while True:
   menuName =  input("Please Enter Menu : ")
   if (menuName.lower() == "exit"):
       break
   else:
        menuList.append([menuName,menu[menuName]])
showBill()


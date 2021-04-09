menuList = []
priceList = []

def showBill():
    result = 0
    print("---- My Food ----")
    for number in range(len(menuList)):
        print(menuList[number],priceList[number])
        result += int(priceList[number])
    print("ราคารวม :", result, "บาท")

while True:
   menuName =  input("Please Enter Menu : ")
   if (menuName.lower() == "exit"):
       break
   else:
        menuPrice = input("Price : ")
        menuList.append(menuName)
        priceList.append(menuPrice)
showBill()



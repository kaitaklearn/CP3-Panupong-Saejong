menuList = []
priceList = []
def showBill():
    result = 0
    print("---- My Food ----")
    for number in range(len(menuList)):
        result += int(menuList[number][1])
        print(menuList[number])
    print("Total :", result)

while True:
   menuName =  input("Please Enter Menu : ")
   if (menuName.lower() == "exit"):
       break
   else:
        menuPrice = input("Price : ")
        menuList.append([menuName,menuPrice])
showBill()


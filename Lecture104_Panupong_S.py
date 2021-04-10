class Customer:  #ชื่อคลาส
    name = ""    #Attribute
    lastname = ""
    age = 0

    def addCart(self):
        print("Add to ",self.name,self.lastname,"cart")
    
Customer1 = Customer()
Customer1.name = "Panupong"
Customer1.lastname = "S"
Customer1.addCart()

Customer2 = Customer()
Customer2.name = "Kodchakorn"
Customer2.lastname = "S"
Customer2.addCart()

Customer3 = Customer()
Customer3.name = "Watcharawit"
Customer3.lastname = "K"
Customer3.addCart()

Customer4 = Customer()
Customer4.name = "Piya"
Customer4.lastname = "C"
Customer4.addCart()
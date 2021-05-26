class Seller:
    def __init__(self):
        self.product_quantity = {}
        self.product_price = {}
        self.profit_price={}
        self.final_profit = 0
    def add_product(self):
        product = input("Enter the name of the product to be added: ")
        product = product.capitalize()
        if product in self.product_quantity.keys():
            ans = input("This item is already present in the inventory do you want to add quantity to this item? : ")
            ans = ans.capitalize()
            if ans == 'No':
                pass
            elif ans == 'Yes':
                answer = input('Do you wish to update the price of the product: ')
                answer = answer.capitalize()
                if answer == 'No':
                  quantity = int(input("Enter the quantity of the product: "))
                  self.product_quantity[product] = int(self.product_quantity[product]) + int(quantity)
                elif answer == 'Yes':
                    quantity = int(input("Enter the quantity of the product: "))
                    purchased_price = int(input("Input the price per unit: "))
                    selling_price = int(input("Enter the price at which the product is to be sold: "))
                    self.product_quantity[product] += int(quantity)
                    self.product_price[product] = selling_price
                    self.profit_price[product] = selling_price - purchased_price
                    print("Product successfully added.")
        else:
            quantity = int(input("Enter the quantity of the product: "))    
            purchased_price = int(input("Input the price per unit: "))
            selling_price = int(input("Enter the price at which the product is to be sold: "))
            self.product_quantity[product]=quantity
            self.product_price[product] = selling_price
            self.profit_price[product] = selling_price - purchased_price
            print("Product added.")
    def show(self):
        for i,j in self.product_quantity.items():
            print(" Product name: ",i,"\n","Quantity: ",j,"\n Price per unit: ",self.product_price.get(i))



class Buyer:
    def __init__(self):
        self.cart={}
        self.total_price=0
    def search(self,seller):
        item_name = input("Enter the name of the product: ")
        item_name = item_name.capitalize()
        if seller.product_quantity.get(item_name):
            print(" Product name: ",item_name,"\n Available units: ",seller.product_quantity.get(item_name))
            print(" Product price: ",seller.product_price.get(item_name))
            choice = input("Do you want to purchase this product?:\n")
            choice = choice.capitalize()
            if choice=="Yes":
                quan = int(input("Enter quantity: "))
                if int(seller.product_quantity.get(item_name)) >= quan:
                    seller.product_quantity[item_name] = int(seller.product_quantity[item_name]) - quan
                    print("You have purchased ",quan," units of ",item_name)
                    print("Your total amount for ",item_name," is ",seller.product_price[item_name]*quan)
                    self.total_price += seller.product_price[item_name] * quan
                    if item_name in self.cart.keys():
                        self.cart[item_name] += quan
                    else:
                        self.cart[item_name] = quan
                    seller.final_profit +=seller.profit_price.get(item_name) * quan
                elif quan > int(seller.product_quantity.get(item_name)):
                    print("Sorry for the inconvenience but this many units of this product is not available,")
                    print("Please select lesser number of units for this product,")
                    print("Available units for the product is: ",seller.product_quantity[item_name])
            else:
                pass
        else:
            print("This item is currently not present in the inventory")
    def cart1(self):
        print("The items in you cart are")
        for i,j in self.cart.items():
            print("Product: ",i,"\n Quantity: ",j)
        print("Your total bill is ",self.total_price)
    def profit(self,seller):
        print("Your overall profit is: ",seller.final_profit," Rupees.")

seller = Seller()
buyer = Buyer()
option = True
while option:
    try:
        print("To exit the program enter exit")
        choice = input("Are you a Buyer or a Seller: ")
        choice = choice.capitalize()
        if choice == "Buyer":
            res = bool(seller.product_quantity)
            if res == True :
                opt = True
                while opt:
                    print("1. Search Items")
                    print("2. Show Cart")
                    print("3. Exit")
                    choice = int(input("Enter your choice: "))
                    if choice == 1:
                        buyer.search(seller)
                    elif choice ==2:
                        buyer.cart1()
                    elif choice == 3:
                        opt = False
                    else:
                        print("Pick a choice from the given options.")
            elif res == False:
                print("\n Please add products to the inventory first. \n")
        elif choice == "Seller":
            opt = True
            while opt:
                print("1. Add Items")
                print("2. Show Items")
                print("3. See profits\loss")
                print("4. Exit")
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    seller.add_product()
                elif choice == 2:
                    seller.show()
                elif choice == 3:
                    buyer.profit(seller)
                elif choice == 4:
                    opt = False
                else:
                    print("Pick a choice from the given options.")
        elif choice == "Exit":
            print("Thank you for shopping with us.")
            print("Exiting from the program...")
            option = False
    except:
        print("Please enter an integer")

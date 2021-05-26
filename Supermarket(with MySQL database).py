import mysql.connector

mydb = mysql.connector.connect(
    host = "host",
    user = "user",
    password = "password",
    database = "supermarket"
)
mycursor = mydb.cursor()
#mycursor.execute ("CREATE TABLE seller_items ( name VARCHAR(255), purchased_price VARCHAR(255), selling_price VARCHAR(255), quantity VARCHAR(255), profit VARCHAR (255))")
class Seller:
        
    def add_product(self):
        product = input("Enter the name of the product to be added: ")
        product = product.casefold()
        mycursor.execute("SELECT * FROM seller_items WHERE name = '{}'".format(product))
        myresult = bool(mycursor.fetchall())
        if myresult == True:
            ans = input("This item is already present in the inventory do you want to add quantity to this item? : ")
            ans = ans.capitalize()
            if ans == 'No':
                pass
            elif ans == 'Yes':
                answer = input('Do you wish to update the price of the product: ')
                answer = answer.capitalize()
                if answer == 'No':
                    quantity = int(input("Enter the quantity of the product: "))
                    sql = "UPDATE seller_items SET quantity = quantity+'{}' WHERE name = '{}'".format(quantity,product)
                    mycursor.execute(sql)
                    mydb.commit()
                    print("Quantity for ",product," updated.")                  
                elif answer == 'Yes':
                    quantity = int(input("Enter the quantity of the product: "))
                    purchased_price = int(input("Input the price per unit: "))
                    selling_price = int(input("Enter the price at which the product is to be sold: "))
                    sql = "UPDATE seller_items SET quantity = quantity+'{}' WHERE name = '{}'".format(quantity,product)
                    mycursor.execute(sql)
                    mydb.commit() 
                    sql = "UPDATE seller_items SET selling_price = '{}' WHERE name = '{}'".format(selling_price,product)
                    mycursor.execute(sql)
                    mydb.commit()
                    sql = "UPDATE seller_items SET purchased_price = '{}' WHERE name = '{}'".format(purchased_price,product)
                    mycursor.execute(sql)
                    mydb.commit()
                    sql = "UPDATE seller_items SET profit = selling_price-purchased_price WHERE name = '{}'".format(product)
                    mycursor.execute(sql)
                    mydb.commit()
                    print("Details for ",product," updated.")
        else:
            quantity = int(input("Enter the quantity of the product: "))    
            purchased_price = int(input("Input the price per unit: "))
            selling_price = int(input("Enter the price at which the product is to be sold: "))
            sql = "INSERT INTO seller_items (name,quantity,purchased_price,selling_price,profit) VALUES ('{}',{},{},{},0)".format(product,quantity,purchased_price,selling_price)
            mycursor.execute(sql)
            mydb.commit()
            print("Product added.")
    def show(self):
        mycursor.execute("SELECT name,quantity,selling_price,purchased_price FROM seller_items")
        myresult = mycursor.fetchall()
        for x,y,z,q in myresult:
            print(" Product Name: ",x,"  Quantity Available: ",y,"  Price: ",q," Selling Price : ",z)
    def record(self):
        name = input("Enter the name of the customer: ")
        name = name.casefold()
        try:
            print("The records for {} are...".format(name))
            mycursor.execute("SELECT name,quantity,price FROM {}".format(name))
            myresult = mycursor.fetchall()
            for x,y,z in myresult:
                print(" Product Name: ",x,"  Quantity Purchased: ",y,"  Price: ",z)
            mycursor.execute("SELECT SUM(price) FROM {}".format(name))
            myresult = mycursor.fetchone()
            print("Grand total for {} is : {}".format(name,myresult))
            rec = input("Do you want to delete this record? : ")
            rec = rec.casefold()
            if rec == "yes":
                sql = "DROP TABLE {}".format(name)
                mycursor.execute(sql)
                print("Record deleted")
            elif rec == "no":
                pass
        except:
            print("The data for {} does not exist.".format(name))
    def inventory(self):
        var = input("Do you wish the clear the whole inventory? : ")
        var = var.casefold()
        if var == "yes":
            sql = "DELETE FROM seller_items"
            mycursor.execute(sql)
            mydb.commit()
            print("Inventory cleared")
        elif var == 'no':
            que = input("Do you wish to remove data for a particular product? : ")
            que = que.casefold()
            if que == 'yes':
                ques = input("Enter the name of the product : ")
                ques = ques.casefold()
                mycursor.execute("SELECT * FROM seller_items WHERE name = '{}'".format(ques))
                myresult = bool(mycursor.fetchall())
                if myresult == True:
                    mycursor.execute("DELETE FROM seller_items WHERE name = '{}'".format(ques))
                    print("Item Deleted")
                else:
                    print("This product is not present in the inventory")
            elif que == 'no':
                pass





class Buyer:
    def search(self,ques):
        item_name = input("Enter the name of the product: ")
        item_name = item_name.casefold()
        mycursor.execute("SELECT * FROM seller_items WHERE name = '{}'".format(item_name))
        myresult = bool(mycursor.fetchall())
        if myresult == True:
            mycursor.execute("SELECT name,quantity,selling_price FROM seller_items WHERE name = '{}'".format(item_name))
            myresult = mycursor.fetchall()
            for a,b,c in myresult:
                print(" Product name: ",a,"\n Available units: ",b)
                print(" Product price: ",c)
                choice = input("Do you want to purchase this product?:\n")
                choice = choice.capitalize()
                if choice=="Yes":
                    quan = int(input("Enter quantity: "))
                    if int(b) >= quan:
                        mycursor.execute("SELECT * FROM {} WHERE name = '{}'".format(ques,item_name))
                        myresult = bool(mycursor.fetchall())
                        if myresult == True:
                            pass
                        else:
                            sql = "INSERT INTO {} (name,quantity,price) VALUES ('{}',0,0)".format(ques,item_name)
                            mycursor.execute(sql)
                            mydb.commit()
                        sql = "UPDATE {} SET quantity = quantity+'{}' WHERE name = '{}'".format(ques,quan,item_name)
                        mycursor.execute(sql)
                        mydb.commit()
                        sql = "UPDATE seller_items SET quantity = quantity-'{}' WHERE name = '{}'".format(quan,item_name)
                        mycursor.execute(sql)
                        mydb.commit()
                        sql = "SELECT selling_price FROM seller_items WHERE name = '{}'".format(item_name)
                        mycursor.execute(sql)
                        myresult = mycursor.fetchone()
                        for x in myresult:
                            sql = "UPDATE {} SET price = price+{}  WHERE name = '{}'".format(ques,int(x)*quan,item_name)
                            mycursor.execute(sql)
                            mydb.commit()   
                        mycursor.execute("SELECT price,quantity FROM {} WHERE name = '{}'".format(ques,item_name))
                        myresult = mycursor.fetchall()   
                        for x,y in myresult:
                            print("You have purchased total ",y," units of ",item_name)
                            print("Your total amount for ",item_name," is ",x)
                        sql = "SELECT selling_price,purchased_price FROM seller_items WHERE name = '{}'".format(item_name)
                        mycursor.execute(sql)
                        myresult = mycursor.fetchall()
                        for x,y in myresult:
                            x = int(x)
                            y = int(y)
                            cal = x-y
                            cq = cal*quan
                            sql = "UPDATE seller_items SET profit = profit + {}  WHERE name = '{}'".format(cq,item_name)
                            mycursor.execute(sql)
                            mydb.commit()
                        print("Product added to cart.")
                    elif quan > int(b):
                        print("Sorry for the inconvenience but this many units of this product is not available,")
                        print("Please select lesser number of units for this product,")
                        mycursor.execute("SELECT quantity FROM seller_items WHERE name = '{}'".format(item_name))
                        myresult = mycursor.fetchall()
                        for x in myresult:
                            print("Available units for the product is: ",x)
                else:
                    pass
        else:
            print("This item is currently not present in the inventory")
    def cart1(self,ques):
        print("The items in you cart are")
        mycursor.execute("SELECT name,quantity,price FROM {}".format(ques))
        myresult = mycursor.fetchall()
        for x,y,z in myresult:
            print(" Product Name: ",x,"  Quantity Purchased: ",y,"  Price: ",z)
        mycursor.execute("SELECT SUM(price) FROM {}".format(ques))
        myresult = mycursor.fetchone()
        print("Your grand total is : ",myresult)
    def profit(self):
        mycursor.execute("SELECT SUM(profit) FROM seller_items")
        myresult = mycursor.fetchall()
        for x in myresult:
            print("Your overall profit is: ",x," Rupees.")
    def overall_display(self):
        print("The available prodcuts are: ")
        mycursor.execute("SELECT name,quantity,selling_price FROM seller_items")
        myresult = mycursor.fetchall()
        for x,y,z in myresult:
            print(" Product Name: ",x,"  Quantity Available: ",y,"  Price: ",z)


seller = Seller()
buyer = Buyer()
option = True
while option:
    try:
        print("To exit the program enter exit")
        choice = input("Are you a Buyer or a Seller: ")
        choice = choice.capitalize()
        if choice == "Buyer":
            ques = input("Please enter your name: ")
            ques = ques.casefold()
            try:
                mycursor.execute("CREATE TABLE {} (name VARCHAR(255), price VARCHAR(255), quantity VARCHAR(255))".format(ques))
            except:
                pass        
            opt = True
            while opt:
                print("1. See available items")
                print("2. Search Items")
                print("3. Show Cart")
                print("4. Exit")
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    buyer.overall_display()
                elif choice == 2:
                    buyer.search(ques)
                elif choice ==3:
                    buyer.cart1(ques)
                elif choice == 4:
                    opt = False
                else:
                    print("Pick a choice from the given options.")
        elif choice == "Seller":
            opt = True
            while opt:
                print("1. Add Items")
                print("2. Show Items")
                print("3. See profits\loss")
                print("4. View Customer record")
                print("5. Remove products")
                print("6. Exit")
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    seller.add_product()
                elif choice == 2:
                    seller.show()
                elif choice == 3:
                    buyer.profit()
                elif choice == 4:
                    seller.record()
                elif choice == 5:
                    seller.inventory()
                elif choice == 6:
                    opt = False
                else:
                    print("Pick a choice from the given options.")
        elif choice == "Exit":
            print("Thank you for shopping with us.")
            print("Exiting from the program...")
            option = False
    except:
        ("Please enter a choice from given options.")

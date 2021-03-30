def update_items():
  product_quantity = input("Enter quantity: ")
  data[product_name] = product_quantity
  print ("\n Product added.")
def show_items():
  for i,j in data.items():
        print ("\n Name = ",i,"\n Quantity = ",j)
def search_items():
  print ("Available quantity of ",key, " is " ,data.get(key), "units.") 
def purchased_items():
  data[purchased_product] = int(data[purchased_product])-units_purchased
  print("The updated number of units for ",purchased_product,"is ",data.get(purchased_product))

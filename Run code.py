import definations.py
data ={}
value = True
option = True
while value:
  print ("\n1. Update Items \n2. Show Items \n3. Search Items  \n4. Purchase Item \n5. Exit")
  try:
    choice = int(input("\n Enter your choice: "))
    if choice ==1:
      while option:
        print("To go to main menu type exit")
        product_name = input("Enter product name: ")
        if product_name == "exit" or product_name == "Exit":
          option = False
        else:
          update_items()      
    elif choice == 2:
      show_items()
    elif choice == 3:
      key = input ("Enter product to be searched: ")
      search_items()
    elif choice == 4:
      purchased_product = input("Enter the name of item you want to buy: ")
      units_purchased = int(input("Enter the number of units purchased: "))
      purchased_items()
    elif choice == 5:
      value = False
    else :
      print ("\n Enter from the given choices")
  except:
    print("Enter a numeric value")

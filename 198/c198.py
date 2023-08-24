while True:
  total = 0
  customer_name = input("Name of the Customer: ")
  while True:
    print("Enter cost of item and quantity")
    cost = float(input("Item cost: "))
    quantity = float(input("item quantity: "))
    total = cost*quantity
    repeat = input("Do you want to add more items? (y/Y/n/N)")
    if repeat == 'n' or repeat == 'N':
      break 
  print("_"*50)
  print("name: ", customer_name)
  print("total bill is: ", total, "free bag")
  print()
  print("Thank You for Shopping with us")
  print("_"*50)
  new_customer = input("Go to next person? (y/Y/n/N)")
  if new_customer == 'n' or new_customer == 'N':
    break

# I Cant Understand how to give u a discount without breaking the code so i guess u can get a free bag
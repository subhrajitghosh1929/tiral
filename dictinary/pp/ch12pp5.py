d = {}
ans = "y"
while ans == "y" or ans == "Y" :
    p_name = input("Enter the product name: ")
    p_price = float(input("Enter product price: "))
    d[p_name] = p_price
    ans = input("Do you want to enter more product names? (y/n): ")
ans = "y"
while ans == "y" or ans == "Y" : 
    name = input("Enter the product name to search: ")
    print("Price:", d.get(name, "Product not found"))
    ans = input("Do you want to know price of more products? (y/n): ")

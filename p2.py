total = 0
menu = {
    "1": {
        "name": "Vegetables",
        "items": {
            "1": {"name": "Tomato", "price": 30},
            "2": {"name": "Potato", "price": 20},
            "3": {"name": "Onion", "price": 25},
            "4": {"name": "Carrot", "price": 35},
            "5": {"name": "Spinach", "price": 40}
        }
    },
    "2": {
        "name": "Fruits",
        "items": {
            "1": {"name": "Apple", "price": 50},
            "2": {"name": "Banana", "price": 40},
            "3": {"name": "Orange", "price": 35},
            "4": {"name": "Grapes", "price": 60},
            "5": {"name": "Mango", "price": 55}
        }
    },
    "3": {
        "name": "Dairy Products",
        "items": {
            "1": {"name": "Milk", "price": 25},
            "2": {"name": "Butter", "price": 45},
            "3": {"name": "Cheese", "price": 60},
            "4": {"name": "Yogurt", "price": 30},
            "5": {"name": "Eggs", "price": 40}
        }
    },
    "4": {
        "name": "Grains",
        "items": {
            "1": {"name": "Rice", "price": 50},
            "2": {"name": "Wheat Flour", "price": 40},
            "3": {"name": "Pasta", "price": 55},
            "4": {"name": "Quinoa", "price": 75},
            "5": {"name": "Oats", "price": 35}
        }
    },
    "5": {
        "name": "Canned Goods",
        "items": {
            "1": {"name": "Canned Beans", "price": 45},
            "2": {"name": "Canned Tomatoes", "price": 40},
            "3": {"name": "Canned Tuna", "price": 55},
            "4": {"name": "Canned Corn", "price": 30},
            "5": {"name": "Canned Soup", "price": 65}
        }
    },
    "6": {
        "name": "Non-Vegetarian",
        "items": {
            "1": {"name": "Chicken Breast", "price": 100},
            "2": {"name": "Pork Steak", "price": 150},
            "3": {"name": "Salmon Fillet", "price": 120},
            "4": {"name": "Lamb Chops", "price": 140},
            "5": {"name": "Caviar", "price": 14000},
            "6": {"name": "Shrimp", "price": 90}
        }
    },
    "": {
        "name":"To print the Final Bill type (B) or 7",
        "items":{
            "B":{"name":"To print the Final Bill","price":total}
        }
    }
}

display_menu = True  

while True:
    if display_menu:
        print("\n\n   M  E  N  U  :")
        print("  ---------------  ")
        for key, value in menu.items():
            print()
            print(f"{key}. {value['name']}")
        print()
    
    choice = input("Enter your choice: ")
    if choice in menu:
        while True:
            print(f"\n\nYou selected {menu[choice]['name']}.")
            print("-" * (len(menu[choice]['name'])+13))
            print("\nItems in", menu[choice]['name'])
            print("-" * (len(menu[choice]['name'])+9))
            for item_key, item_value in menu[choice]['items'].items():
                print(f"{item_key}. {item_value['name']}\t -\t INR {item_value['price']}")
            print("M to return to the main menu.")
            print()
            item = input("Enter the item no.: ")
            if item in menu[choice]['items']:
                if item == "M":
                    display_menu = True  # Set to display the main menu again
                    break
                dish = float(input("Enter the amount(in KG.): "))
                price = menu[choice]['items'][item]['price'] * dish
                total += price
                print("INR.", total)
            elif item == "M":
                display_menu = True  # Set to display the main menu again
                break
            else:
                print("Invalid item number")
    elif choice == "B" or choice == "7":
        print("\n\nYour final bill is INR", total)
        print("Hope you had a splendid experience.")
        print("Thank you for visiting, hoping to meet you soon.")
        print("\nExiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

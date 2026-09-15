total=0
while True:
    print("\n\n   M  E  N  U  :")
    print("  ------------  ")
    print("1. Indian Cuisine Classics ")
    print("2. Continental ")
    print("3. Stacks and Wraps")
    print("4. World kitchen")
    print("5. Confectionaries")
    print("6. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        while True:
            print("\n\nYou selected Indian Cuisine Classics.")
            print("-------------------------------------")
            print("\nItems in  Indian Cuisine Classics.")
            print(" 1.  Paneer ajwaini tikka ")
            print(" 2.  Murgh tikka ")
            print(" 3.  Paneer makhni")
            print(" 4.  Subz kadhai")
            print(" 5.  Khoya mewa kofta ")
            print(" 6.  Bhare alu dum ")
            print(" 7.  Murgh tikka makhani")
            print(" 8.  Mutton rogan josh")
            print(" 9.  Dal makhiani")
            print(" 10. Macher jhol")
            print(" 11. Exit")
            item = input("Enter your item no.: ")
            if item == "1":
                print("Presenting paneer ajwani tikka for your delight")
                print("an all time classic of a fresh cottage cheese")
                print("cubes marinated in Bengal gram flour and")
                print("select spices, cooked in tandoor.")
                print("INR 625")
            elif item == "2":
                print("Presenting Murgh tikka for your delight")
                print("juicy morsels of boneless chicken marinated in")
                print("yoghurt and select spices cooked in tandoor.")
                print("INR 675")
            elif item == "3":
                print("Presenting paneer makhni for your delight")
                print("fresh cotton cheese simmered in rice tomato and")
                print("cshwnut gravy,flavoured with fenugreek")
                print("INR 875")
            elif item == "4":
                print("Presenting subz kadhi for your delight")
                print("season's bounty of vegetable cooked on low fire")
                print("with desi ghee and fine spices in a special cast- iron")
                print("'kadhi' that imparts an irresistible flavour and goodness")
                print("INR 875")
            elif item == "5":
                print("Presenting khoya mewa kofta for your delight")
                print("crispy khoya marble stuffed with nuts simmered in cashewnut gravy")
                print("INR 875")
            elif item == "6":
                print("Presenting bhare alu dum for your delight")
                print("scooped potatoes filled with spiced crisp potato")
                print("hash with boiled walnut mixture napped in cude and brown onion gravy")    
                print("875")
            elif item == "7":
                print("Presenting murgh tikka makhani for your delight")
                print("char-grilled chicken tikka simmered in a robust tomato")
                print("and cashewnut gravy,flavoured with dried fenugreek")
                print("leaves finished with unsalted butter and fresh cream")
                print("INR 975")
            elif item == "8":
                print("Presenting mutton rogan josh for your delight")
                print("select cuts of mutton cooked in a thick and flvoursome")
                print("gravy with the goodness of whole spices")
                print("INR 1150")
            elif item == "9":
                print("Presenting dal makhiani for your delight")
                print("overnight simmered slow cooked lentils cooked ")
                print("with ginger, garlic, toomato puree, enriched with cream")
                print("and finished with unsalted butter")
                print("INR 675")
            elif item == "10":
                print("Presenting macher jhol for your delight")
                print("lightly marinated fresh water fish, fried then simmered")
                print("with pieces of cauliflower, potatoes and aubergine")
                print("in a thin gravy made with cumin, onion seed and mustard oil")
                print("INR 1025")
            elif item=="11":
                print("Indian Cuisine Classics is over")
                break
            dish = int(input("Enter the no. of dish(es): "))
            price=0
            if item == "1":
                price= 625*dish
                #dp51=625
                #dis51=dish
                #ch51=1
            elif item=="2" :
                price= 675*dish
                #dp52=675
            elif item=="3":
                price= 875*dish
                #dp53=875
            elif item=="4":
                price= 875*dish
                #dp54=875
            elif item=="5" :
                price= 875*dish
                #dp52=875
            elif item=="6":
                price= 875*dish
                #dp53=875
            elif item=="7":
                price= 975*dish
                #dp54=975
            elif item=="8":
                price= 1150*dish
                #dp54=1150
            elif item=="9":
                price= 675*dish
                #dp54=675
            elif item=="10":
                price= 1025*dish
                #dp54=1025
            total=total+price
            print("INR. ",total) 
    elif choice == "2":
        while True:
            print("\n\nYou selected Continental ")
            print("------------------------ ")
            print("\nItems in Continental")
            print(" 1. Subz tehri ")
            print(" 2. Mentiaburz gosht biryani ")
            print(" 3. Chicken biryani ")
            print(" 4. Mutton biryani ")
            print(" 5. Exit")
            item = input("Enter your item no.: ")
            if item == "1":
                print("Presenting subz tehri for your delight")
                print("sesonal vegetable cooked with long grain basmati rice ")
                print("and select Indian spices")
                print("INR 875")
            elif item == "2":
                print("Presenting Mentiaburz gosht biryani for your delight")
                print("kolkata's traditional basati rice biryani of potatoes")
                print("egg and mutton")
                print("INR 1150")
            elif item == "3":
                print("Presenting chicken biryani for your delight")
                print("INR 500")
            elif item == "4":
                print("Presenting mutton biryani for your delight")
                print("INR 650")
            elif item=="5":
                print("Continental  is over")
                break
            dish = int(input("Enter the no. of dish(es): "))
            price=0
            if item == "1":
                price= 875*dish
                #dp51=875
                #dis51=dish
                #ch51=1
            elif item=="2" :
                price= 1150*dish
                #dp52=1150
            elif item=="3":
                price= 500*dish
                #dp53=500
            elif item=="4":
                price= 650*dish
                #dp54=650
            total=total+price
            print("INR. ",total)
    elif choice == "3":
        while True :
            print("\n\nYou selected Stacks and Wraps.")
            print("------------------------------")
            print("\nItems in  Stacks and Wraps")
            print(" 1. Veggie club ")
            print(" 2. Classic club ")
            print(" 3. Chickpea and spinach patty burger ")
            print(" 4. Chicken katsu burger ")
            print(" 5. Classic lamp patty burger ")
            print(" 6. Exit")
            item = input("Enter your item no.: ")
            if item == "1":
                print("Presenting veggie club for your delight")
                print("A double tosted sandwitch of grilled zucchini")
                print("confit tomatoes, roast peppers, maple glazed onions")
                print("and red cheddar cheese ")
                print("INR 700")
            elif item == "2":
                print("Presenting classic club for your delight")
                print("A toased double decker classic sandwich of chicken")
                print("salad, smoked bacon, fried egg and emmental")
                print("INR 850")
            elif item == "3":
                print("Presenting chickpea and spinach patty burger for your delight")
                print("maple glazed onions and dalle chilli aioli")
                print("INR 725")
            elif item == "4":
                print("Presenting chicken katsu burger for your delight")
                print("pepper jam and garri")
                print("INR 850")
            elif item == "5":
                print("Presenting classic lamp patty burger for your delight")
                print("fried egg and red onion tartare")
                print("INR 950")
            elif item=="6":
                print("Stacks and Wraps is over")
                break
            dish = int(input("Enter the no. of dish(es): "))
            price=0
            if item == "1":
                price= 700*dish
                dp51=700
                dis51=dish
                ch51=1
            elif item=="2" :
                price= 850*dish
                dp52=850
            elif item=="3":
                price= 725*dish
                dp53=725
            elif item=="4":
                price= 850*dish
                dp54=850
            elif item=="5":
                price= 950*dish
                dp55=545
            total=total+price
            print("INR. ",total)
        
    elif choice == "4":
        while True:
            print("\n\nYou selected World kitchen.")
            print("----------------------------")
            print("\nItems in World kitchen. ")
            print(" 1. vagetable Fricassee ")
            print(" 2. grilled chicken ")
            print(" 3. spagatti agli,olio e peperroncino ")
            print(" 4. green pea and saffron risotto ")
            print(" 5. penne arrabbiate with chicken ")
            print(" 6. Exit")
            item = input("Enter your item no.: ")
            if item == "1":
                print("Presenting vagetable Fricassee for your delight")
                print("garden fresh exotic vegetables cooked with")
                print("bechamel sauce and flavoured with fresh herbs")
                print("INR 875")
            elif item == "2":
                print("Presenting grilled chicken for your delight")
                print("marinated chicken, grilled and served with mashed")
                print("potatoes and black pepper jus")
                print("INR 975")
            elif item == "3":
                print("Presenting spagatti agli,olio e peperroncino for your delight")
                print("spaghetti tossed in olive oil along with candied")
                print("garlic nd chili flaked, seasoned to perfection")
                print("INR 775")
            elif item == "4":
                print("Presenting green pea and saffron risotto for your delight")
                print("fresh peas and saffron infused creamy risotto")
                print("finished with parmesan and butter")
                print("INR 775")
            elif item == "5":
                print("Presenting penne arrabbiate with chicken for your delight")
                print("teder chicken cooked with penned pasta in a spicy")
                print("tomato concasse and red chili flakes infused arrabbita sauce ")
                print("INR 825")
            elif item=="6":
                print("World kitchen is over")
                break
            dish = int(input("Enter the no. of dish(es): "))
            price=0
            if item == "1":
                price= 875*dish
                dp51=875
                dis51=dish
                ch51=1
            elif item=="2" :
                price= 975*dish
                dp52=975
            elif item=="3":
                price= 775*dish
                dp53=775
            elif item=="4":
                price= 775*dish
                dp54=775
            elif item=="5":
                price= 825*dish
                dp55=825
            total=total+price
            print("INR. ",total)
    elif choice == "5":
        while True:
            print("\n\nYou selected Confectionaries .")
            print("-------------------------------")
            print("\nItems in Confectionaries ")
            print("1. Baked cheesecake")
            print("2. Walnut brownie")
            print("3. Gulab jamun ")
            print("4. Mung dal halwa")
            print("5. Chocolates doughnuts ")
            print("6. Muffins ")
            print("7. to exit Confectionaries ")
            item = input("Enter your item no.: ")
            if item == "1":
                print("Prsenting Baked cheesecake for your delight ")
                print("white choclate and cream cheese baked cheesecake ")
                print("INR 545")
            elif item == "2":
                print("Prsenting Walnut brownie for your delight ")
                print("fudgy chocolate brownie with walnuts ")
                print("INR 545")
            elif item == "3":
                print("Prsenting gulab jamun for your delight ")
                print("deep fried milk solids soaked in sugar syrup ")
                print("INR 545")
            elif item == "4":
                print("Prsenting Mung dal halwa for your delight")
                print("mouhwatering halwa of mung bean lentil, slow cooked in desi ghee wth nuts")
                print("INR 175")
            elif item == "5":
                print("Prsenting Chocolates doughnuts for your delight")
                print("INR 175")
            elif item == "6":
                print("Prsenting Muffins for your delight ")
                print("INR 175")
            elif item=="7":
                print("option 5 is over")
                break
            dish = int(input("Enter the no. of dish(es): "))
            price=0
            if item == "1":
                price= 545*dish
                dp51=545
                dis51=dish
                ch51=1
            elif item=="2" :
                price= 545*dish
                dp52=545
            elif item=="3":
                price= 545*dish
                dp53=545
            elif item=="4":
                price= 175*dish
                dp54=545
            elif item=="5":
                price= 175*dish
                dp55=545
            elif item=="6":
                price= 175*dish
                dp56=545
            total=total+price
            print("INR. ",total)
    elif choice == "6":
        print("\n\nYour final bill is INR ",total)
        print("Hope you had a splendid experiance. ")
        print("Thankyou for visiting, hopping to meet you soon. ")
        print("\nExiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

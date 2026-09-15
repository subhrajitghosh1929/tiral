val=[17,23,18,19]
print("the list is:",val)
while True:
    print("main menue")
    print("1.insert")
    print("2.delete")
    print("3.exit")
    ch=int(input("Enter your choice1/2/3 "))
    if ch==1:
        item=int(input("Enter item "))
        pos=int(input("insert at which position "))
        index=pos-1
        val.insert(index,item)
        print("success! list now is: ",val)
    elif ch==2:
        print("delete menue ")
        print("1.delete using value ")
        print("2.delete using index ")
        print("3.delete a sublist ")
        dch=int(input("enter choice (1 or 2 or 3) "))
        if dch==1:
            item=int(input("enter item to be deleted : "))
            val.remove(item)
            print("list now is:",val)
        elif dch==2:
            index=int(input("Enter index of item to be deleted "))
            val.pop(index)
            print("list now is:",val)
        elif dch==3:
            l=int(input("Enter lower limit of list to be deleted "))
            h=int(input("Enter upper limit of list to be deleted "))
            del val[l:h]
            print("list now is: ",val)
        else:
            print("valid choice are 1/2/3 only ")
    elif ch==3:
        break
    else:
        print("valid choice are 1/2/3 only")


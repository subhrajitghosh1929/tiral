"""Stack : implement as a list
top: integer having position of topmost element in stack
"""
def isEmpty(stk):
    if stk==[]:
        return True
    else:
        return False
def Push (stk, item):
    stk.append(item)
    top=len(stk)-1
def pop(stk):
    if isEmpty(stk):
        return "Underflow"
    else:
        item = stk.pop()  # Remove the top item
        if len(stk) == 0:
            top = None
        else:
            top = len(stk) - 1  # Update the top pointer correctly
        return item  # Return the removed item

def peek(stk):
    if isEmpty(stk):
        return"Underflow"
    else:
        top=len(stk)-1
        return stk[top]
def display(stk):
    if isEmpty(stk):
        print("Stack empty")
    else:
        top=len(stk)-1
        print(stk[top],"<-top")
        for a in range (top-1,-1,-1):
            print(stk[a])
#main
Stack=[]
top=None
while True:
    print("STACK OPERATIONS")
    print("1.Push")
    print("2.Pop")
    print("3.Peek")
    print("4.Dispay stack")
    print("5.Exit")
    ch=int(input("Enter your choice(1-5):"))
    if ch==1:
        item=int(input("Enter item:"))
        Push(Stack,item)
    elif ch==2:
        item=pop(Stack)
        if item=="Underflow":
            print("Underflow!Stack is empty!")
        else:
            print("Poppend item is",item)
    elif ch==3:
        item=peek(Stack)
        if item=="Underflow":
            print("Underflow!Stack is empty!")
        else:
            print("Topmost item is",item)
    elif ch==4:
        display(Stack)
    elif ch==5:
        break
    else:
        print("Invalid choice!")
        

















                    

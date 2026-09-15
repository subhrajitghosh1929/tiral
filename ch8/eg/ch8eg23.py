# gussing game
import random
n=random.randint(10,50)
ctr=0
print("guess a number in range 10..50 :")
while ctr<5:
    print("trial number : ",ctr+1)
    guess= int(input("guess your number :"))
    if guess==n:
        print("you win!!:)",n)
        break
    elif n-5<guess and guess<n+5 :
        print("you are near ")
    else:
        print("wild guess ")
    ctr+=1
if not ctr <5:
    print("you lose:(\n the number was",n)

import random
secretNum= random.randint(1,100)
guessNumString=int(input("Guess a number between 1 and 100 inclusive: "))
while guessNumString !=secretNum:
    if guessNumString<secretNum:
        print("your guess is too low")
    else:
        print("your guess is too high")
    guessNum=int(input("Guess a number between 1 and 100 inclusive: "))
print("congratulation ! You guess the correct number")
        
 

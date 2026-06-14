'''
1 for stone
-1 for paper
0 for scissor'''
import random

computer = random.choice([1,-1,0])
youstr = input("Enter your choice: ")
youDict = {"s":1,"p":-1,"c":0}
reverseDict = {1:"stone",-1:"paper",0:"scissor"}
you = youDict[youstr]

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if(computer == you):
    print("It's a draw")

else:
    if(computer == -1 and you == 1):
        print("You lose")
    
    elif(computer == -1 and you == 0):
        print("You Won")

    elif(computer ==1 and you == -1):
        print("You Won")

    elif(computer ==1 and you==0):
        print("You lose")
    elif(computer==0 and you==-1):
        print("You lose")

    elif(computer==0 and you==1):
        print("You Won")

    else:
        print("somthing went wrong")



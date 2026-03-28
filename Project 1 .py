#SNAKE WATER GUN GAME
import random
''' 
1 for snake 
0 for water 
-1 for gun
'''
computer= random.choice([1,0,-1])
youstr =input("enter your choice: ")
youDict = {"s": 1, "w": 0, "g": -1}
reverseDict = {1: "snake", 0: "water", -1: "gun"}
you = youDict[youstr]
print(f"you choice is {reverseDict[you]}\ncomputer choice is {reverseDict[computer]}")
if you == computer:
    print("it is a tie")
elif (you == 1 and computer == 0) or (you == 0 and computer == -1) or (you == -1 and computer == 1):
    print("you win")
else:   print("you lose")
print("thanks for playing")

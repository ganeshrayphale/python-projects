"""
1 : rock 
0: paper 
-1: scissors
"""
import random  # importing libraray for random number generation

computer_choice =random.choice([1,0,-1]) # genrating random integer form computer

choice=input("Enter your choice (rock, paper, scissors): ").lower()# taking input from user

dict={"rock":1,"paper":0,"scissors":-1} 
revdict={1:"rock",0:"paper",-1:"scissors"}  
print(f"you choosed :{choice}")
print(f"computer choosed : {revdict[computer_choice]}")


if dict[choice]== computer_choice:
    print("It's a Draw")
else:
    if dict[choice]==1 and computer_choice==0:
        print("You lose")
    elif dict[choice]==1 and computer_choice==-1:
        print("You win")
    elif dict[choice]==0 and computer_choice==1:
        print("You win")
    elif dict[choice]==0 and computer_choice==-1:
        print("You lose")
    elif dict[choice]==-1 and computer_choice==1:
        print("You lose")
    elif dict[choice]==-1 and computer_choice==0:
        print("You win")
    else:
        print("Invalid input")




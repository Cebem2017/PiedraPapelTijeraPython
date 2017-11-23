import random
player1=0
player2 =0

player1 = input("Player 1= Rock(1), paper(2) or scissors(3):")

player2 = input("Player 2= Rock(1), paper(2) or scissors(3):")

print("Rock(1), paper(2) or scissors(3)")
print("Player 1 selected option "+player1)
print("Player 2 selected option "+player2)

if player1==player2:
    print("Draw")
elif player1 == "1" and player2 =="3":
     print("Player 1 win")
elif player1 == "1" and player2=="2" :
     print("Player 2 win")
elif player1 == "2" and player2 =="1":
     print("Player 1 win")
elif player1 == "2" and player2 =="3":
    print("Player 2 win")
elif player1 == "3" and player2 =="2":
    print("Player 1 win")
elif player1 == "3" and player2 =="1":
    print("Player 2 win")
    
print("End of game")   

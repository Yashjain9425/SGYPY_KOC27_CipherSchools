import random
score=0
while(True):
    print(" _______________________")
    print("|     ***MENU***        |")
    print("|                       |")
    print("|  1.PLAY               |")
    print("|  2.SCORE              |")
    print("|  3.EXIT               |")
    print("|                       |")
    print("|_______________________|")
    opt=int(input())
    if(opt==1):
        ui=int(input("ENTER A STATIC NUMBER(from 1 to 6)\n"))
        dice=random.randint(1,6)
        print("DICE=",dice)
        if(ui==dice):
            print("YOU WIN")
            score=score+1
        else:
            print("YOU LOSE")
        print("YOUR SCORE =",score)
    elif(opt==2):
        print("SCORE =",score)
    elif(opt==3):
        print("THANK YOU FOR PLAYING")
        break
    else:
        print("INVALID INPUT(CHOOSE OPTION FROM 1 TO 3)")

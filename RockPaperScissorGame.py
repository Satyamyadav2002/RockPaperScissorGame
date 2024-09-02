import random
l=["Rock","Paper","Scissor"]
while True:
    ccount=0
    ucount=0
    uc=int(input('''
Game Start...
1 Yes
2 No | Exit
'''                 
))
    if uc==1:
        for a in range(1,6):
            userInput=int(input('''
1 Rock
2 Paper
3 Scissor
'''
))
            if userInput==1:
                uchoice="Rock"
            elif userInput==2:
                uchoice="Paper"
            elif userInput==3:
                uchoice="Scissor"
            Cchoice=random.choice(l)
            if Cchoice==uchoice:
                print("Computer value:-",Cchoice)
                print("User value:-",uchoice)
                print("Game Draw")
                ucount=ucount+1
                ccount=ccount+1
            elif ((uchoice=="Rock" and Cchoice=="Scissor") or (uchoice=="Paper"  and Cchoice=="Rock") or (uchoice=="Scissor" and Cchoice=="paper")):
                print("Computer value:-",Cchoice)
                print("User value:-",uchoice)
                print("You Win")
                ucount=ucount+1
            else:
                print("Computer value:-",Cchoice)
                print("User value:-",uchoice)
                print("Computer Win")
                ccount=ccount+1
        if ucount==ccount:
            print("Final Game Draw")
            print("User Score:-",ucount)
            print("Computer Score:-",ccount)
        elif ucount>ccount:
            print("You Win The Game...")
            print("User Score:-",ucount)
            print("Computer Score:-",ccount)
        else:
            print("Computer Win The Game...")
            print("User Score:-",ucount)
            print("Computer Score:-",ccount)
    else:
        break

                

                

         


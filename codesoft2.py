import random
options=['rock','paper','scissor']
comp=random.choice(options)
player=input("Enter your choice:")
if comp==player:
    print("It's a tie!!")
else :
    if player=='rock':
        if comp=='paper':
            print("computer won")  
        else:
            print("you win")

    else:
        if player=='paper':
         if comp=='scissor':
            print("computer won")
         else:
            print("You win") 

        else:
         if player=='scissor':
          if comp=='rock':
            print("computer won")
         else:
            print("You win") 

    
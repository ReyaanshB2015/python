import random
while True:
    function_action=input("choose your option rock,paper and scissors")
    possible_action= ["rock","paper","scissors"]
    ca=random.choice(possible_action)
    print("you chose ",function_action, " computer chose ",ca)
    if function_action==ca:
        print("both the players have selected ",function_action)
    elif ca=="rock":
        if function_action=="scissors":
            print("rock wins!!")
        else:
            print("paper wins!!")
    elif ca=="paper":
        if function_action=="rock":
            print("paper wins!!")
        else:
            print("scissors wins!!")
    elif ca=="scissors":
        if function_action=="paper":
            print("scissors wins!!")
        else:
            print("rock wins!!")
    pa =input("Want to play again -y/n")
    if pa!="Y" and pa !="y":
      break
                    
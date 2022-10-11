print("welcome to Treasure Island \n Your mission is to find the treasure.")
direction=input("You are at a crossroad, where do you want to go? Type 'left' or 'right'\n")
if direction=='right':
    print("You fell into a hole. GAME OVER")
if direction=='left':
    step1=input("Lake in your way do you want to wait or swim?\n")
    if step1=='swim':
        print("You are attacked by a trout. GAME OVER")
    if step1=='wait':
        step2=input("You have 3 doors in front of you Red, Yellow and Blue. Where doyou want to enter?\n")
        if step2=='Red':
            print("You burned by fire. GAME OVER")
        elif step2=='Blue':
            print("You are eaten by beasts. GAME OVER")
        elif step2=='Yellow':
            print("YOU WIN!")
        else: print("GAME OVER")
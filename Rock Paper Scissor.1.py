import random
user_action=input("Enter your choice(rock,paper,scissor):")
possible_actions=["rock","paper","scissors"]
computer_action=random.choice(possible_actions)
print(f"\nyou chose{user_action},computer chose{computer_action}.\n")
if user_action==computer_action:
    print(f"both player selected{user_action}.it's a tie")
elif user_action=="rock":
    if computer_action=="scissors":
       print("rock smash scissor you win")
    else:
       print("paper cover rock you lose")
elif user_action=="paper":
    if computer_action=="rock":
       print("paper cover rock you win")
    else:
       print("scissors cuts paper you lose")
elif user_action=="scissor":
    if computer_action=="paper":
       print("scissor cuts paper you win")
    else:
        print("rock smash scissor you lose")

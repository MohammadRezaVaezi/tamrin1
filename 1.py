import random
items = ["rock", "paper", "scissor"]
# index = random.randint(0, 2)
# computer_choice = items[index]
score_user = 0
score_computer = 0
while score_user != 5 or score_computer != 5:
    computer_choice = random.choice(items)
    print("0-rock")
    print("1-paper")
    print("2-scissor")
    user_choice_index = int(input("please choose the item "))
    user_choice = items[user_choice_index]
    if computer_choice == "rock" and user_choice == "scissor":
        print("computer choice is " + computer_choice)
        print("computer win ")
        score_computer += 1
        print("computer = " + str(score_computer) + " " + "you = " + str(score_user))
    elif computer_choice == "rock" and user_choice == "rock":
        print("computer choice is " + computer_choice)
        print("tied")
        print("computer = " + str(score_computer) + " " + "you = " + str(score_user))
    elif computer_choice == "rock" and user_choice == "paper":
        print("computer choice is " + computer_choice)
        print("user win")
        score_user += 1
        print("computer = " + str(score_computer) + " " + "you = " + str(score_user))
    elif computer_choice == "paper" and user_choice == "rock":
        print("computer choice is " + computer_choice)
        print("computer win")
        score_computer += 1
        print("computer = " + str(score_computer) + " " + "you = " + str(score_user))
    elif computer_choice == "paper" and user_choice == "paper":
        print("computer choice is " + computer_choice)
        print("tied")
        print("computer = " + str(score_computer) + " " + "you = " + str(score_user))
    elif computer_choice == "paper" and user_choice == "scissor":
        print("computer choice is " + computer_choice)
        print("user win")
        score_user += 1
        print("computer = " + str(score_computer) + " " + "you = " + str(score_user))
    elif computer_choice == "scissor" and user_choice == "rock":
        print("computer choice is " + computer_choice)
        print("user win")
        score_user += 1
        print("computer = " + str(score_computer) + " " + "you = " + str(score_user))
    elif computer_choice == "scissor" and user_choice == "paper":
        print("computer choice is " + computer_choice)
        print("computer win")
        score_computer += 1
        print("computer = " + str(score_computer) + " " + "you = " + str(score_user))
    else:
        print("computer choice is " + computer_choice)
        print("tied")
        print("computer = " + str(score_computer) + " " + "you = " + str(score_user))
    if score_user == 5:
        print("user win")
        exit()
    elif score_computer == 5:
        print("user lose")
        exit()

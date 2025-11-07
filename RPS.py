import random


def rps():

    bot = ["Rock", "Paper", "Scissors"]
    score = 0
    player_choice = 1
    while (player_choice != 0):
        print("1= Rock", "2= Paper", "3= Scissors")
        try:
            player_choice = int(input("First Player : "))
            bot_choice = random.choice(bot)
            print("Bot : " + bot_choice)
        except ValueError:
            print("*******Error!********")

        if player_choice > 3:
            print("****Not an option!!****")

        elif player_choice == 1:
            if bot_choice == "Rock":
                print("***Draw!***")
            elif bot_choice == "Paper":
                print("***Win!***")
                score += 1
            else:
                print("***Wrong!***")

        elif player_choice == 2:
            if bot_choice == "Rock":
                print("***Win!***")
                score += 1

            elif bot_choice == "Paper":
                print("***Draw!***")
            else:
                print("***Wrong!***")

        elif player_choice == 3:
            if bot_choice == "Rock":
                print("***Wrong!***")
            elif bot_choice == "Paper":
                print("***Win!***")
                score += 1
            else:
                print("***Draw!***")

        else:
            break
        print(f"Score: {score}")
        # print("Score : " + str(score))

    return score


print(rps())

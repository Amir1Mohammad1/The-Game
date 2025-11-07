import random
import time
import pandas
import numpy

def select_game():
    menu = ('M', 'R', 'P', 'S', 'E')
    score = 0

    while True:
        print('**********Welcome**********')
        print('M = Menu')
        print('R = rock paper scissors')
        print('P = Pop Quiz')
        print('S = Score')
        print('E = Exit')
        print()
        user_input = input('Enter an option: ').upper()

        if user_input in menu:
            break
        else:
            print()
            print('Invalid input. Please try again.')
    if user_input == 'M':
        print('Loading......')
        time.sleep(2)
        print('Welcome to Menu :)')
        print(("----------------------"))
        print(select_game())
    elif user_input == 'R':
        print('Loading......')
        time.sleep(2)
        print('Welcome to Rock Paper Scissors :)')

        print("----------------------")

        def rps():

            bot = ["Rock", "Paper", "Scissors"]
            score = 0
            player_choice = 1
            while (player_choice != 0):
                print("1= Rock", "2= Paper", "3= Scissors", "0= Exit")
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

                elif player_choice == 0:
                    print("Thanks for playing!")
                    print(f"Your Current Score: {score}")
                    print(select_game())

                else:
                    break
                print(f"Score: {score}")
                # print("Score : " + str(score))

            return score

        print(rps())

    elif user_input == 'P':
        print('Loading......')
        time.sleep(2)
        print('Welcome to Pop Quiz :)')

        def pop_q():
            questions = ("How many elements are in the periodic table?: ",
                         "Which animal lays the largest eggs?: ",
                         "What is the most abundant gas in Earth's atmosphere?: ",
                         "How many bones are in the human body?: ",
                         "Which planet in the solar system is the hottest?: ")

            options = (("A. 116", "B. 117", "C. 118", "D. 119"),
                       ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
                       ("A. Nitrogen", "B. Oxygen",
                        "C. Carbon-Dioxide", "D. Hydrogen"),
                       ("A. 206", "B. 207", "C. 208", "D. 209"),
                       ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

            answers = ("C", "D", "A", "A", "B")
            guesses = []
            score = 0
            question_num = 0

            for question in questions:
                print("----------------------")
                print(question)
                for option in options[question_num]:
                    print(option)

                guess = input("Enter (A, B, C, D): ").upper()
                guesses.append(guess)
                if guess == answers[question_num]:
                    score += 1
                    print("CORRECT!")

                else:
                    print("INCORRECT!")
                    print(f"{answers[question_num]} is the correct answer")
                question_num += 1

                if guess == 0:
                    print(select_game())

            print("----------------------")
            print("       RESULTS        ")
            print("----------------------")

            print("answers: ", end="")
            for answer in answers:
                print(answer, end=" ")
            print()

            print("guesses: ", end="")
            for guess in guesses:
                print(guess, end=" ")
            print()

            score = int(score / len(questions) * 100)
            print(f"Your score is: {score}%")

        print(pop_q())

    elif user_input == 'S':
        print('Calculating.....')
        time.sleep(2)
        print(f'Your current score is: {score}')
        print(select_game())

    elif user_input == 'E':
        print('Exiting.....')
        time.sleep(2)
        exit()

    else:
        print('try again')


print(select_game())

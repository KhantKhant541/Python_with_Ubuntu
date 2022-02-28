import random


def game_play(num):
    score = []
    name = []
    for i in range(num + 1):
        correct_number = random.randint(1, 100)
        player_name = input("Enter your name : ")
        guess_time = 0
        while correct_number:
            guess_number = int(input("Enter your guess number : "))

            if guess_number < correct_number:
                print(f"Guess higher than {guess_number}")
                guess_time += 1

            elif guess_number > correct_number:
                print(f"Guess lower than {guess_number}")
                guess_time += 1

            else:
                print("Congratulation you get the correct number!")
                break
        print(f"You guessed {guess_time} times.")
        score.append(guess_time)
        name.append(player_name)
        print("Your score is successfully recorded!")
    min_score = min(score)
    winner = name[score.index(min_score)]
    print(f"Winner is {winner} with minimum score of {min_score}")


def main():
    no_of_player = int(input("How many player want to play : "))
    game_play(no_of_player)


if __name__ == "__main__":
    main()

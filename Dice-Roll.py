import random


def dice_roll():
    dicerolls = random.randint(1,6) # randomly chooses a number for the dice
    return dicerolls


def game():
    p1 = 0 # player 1
    p1_wins = 0 # player 1 win count
    p2 = 0 # player 2
    p2_wins = 0 # player 2 win count
    rounds = 1 # rounds in dice game

    while rounds != 8:
        print(f"Round: {rounds}" )
        p1 = dice_roll()
        p2 = dice_roll()

        print(f"Player 1 Roll: {p1} " )
        print(f"Player 2 Roll: {p2} " )

        if p1 == p2:
            print("Draw!")

        elif p1 > p2:
            p1_wins += 1
            print("P1 Wins!")
        else:
            p2_wins += 1
            print("P2 Wins!")
        rounds += 1

    if p1_wins == p2_wins:
        print("Draw Overall!")
    elif p1_wins > p2_wins:
        print(f"P1 won this many rounds: {p1_wins}")
    else:
        print(f"P2 won this many rounds: {p2_wins}")



game()
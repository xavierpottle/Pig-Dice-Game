import random

def roll():
    return random.randint(1, 6)

# Get number of players
while True:
    players = input("Enter the number of players (2 - 4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Number must be between 2 - 4.")
    else:
        print("Invalid input, please enter a number.")

# Game setup
max_score = 50
player_scores = [0 for _ in range(players)]

# Game loop
while max(player_scores) < max_score:
    for player_index in range(players):
        print(f"\nPlayer {player_index + 1}'s turn!")
        print("Your total score is:", player_scores[player_index])

        current_score = 0

        while True:
            should_roll = input("Would you like to roll (y)? ")
            if should_roll.lower() != "y":
                break
            value = roll()
            print("You rolled a:", value)
            if value == 1:
                print("You rolled a 1! Turn over, no points added.")
                current_score = 0
                break
            else:
                current_score += value
                print("Your score this turn is:", current_score)

        player_scores[player_index] += current_score
        print("Your total score is now:", player_scores[player_index])

        if player_scores[player_index] >= max_score:
            break  # Exit early if someone wins

# Determine winner
max_score = max(player_scores)
winning_index = player_scores.index(max_score)
print("\n🏆 Player", winning_index + 1, "wins with a score of:", max_score)

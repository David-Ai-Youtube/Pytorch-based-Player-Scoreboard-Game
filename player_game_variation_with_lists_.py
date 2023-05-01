#This code is a variation of the previous one that uses PyTorch tensors instead of Python lists for the scores and elimination status. 
#The main differences are that the code uses PyTorch functions for array operations, such as torch.zeros to initialize the scores and 
#elimination status, and torch.argmax to find the player with the highest score or that hasn't been eliminated. 
#The code is similar in structure and implements the same game logic with the same win and elimination conditions.

import time
from IPython.display import clear_output

# initialize the scores and elimination status for each player
scores = [0, 0, 0, 0]
eliminated = [False, False, False, False]

while True:
    # check if any player has reached a score of 10
    if 10 in scores:
        winner = scores.index(10)
        clear_output(wait=True)
        print(f"Player{winner+1} has won with a score of {scores[winner]}. Game over.")
        break

    # check if all but one player have been eliminated
    if eliminated.count(False) == 1:
        winner = eliminated.index(False)
        clear_output(wait=True)
        print(f"Player{winner+1} has won with a score of {scores[winner]}. Game over.")
        break

    # generate a new tensor with 4 values, representing the scores for each player
    a = torch.rand(4)

    # update the scores and elimination status for each player based on the tensor values
    for i, val in enumerate(a):
        if eliminated[i]:
            continue
        if val > 0.5:
            scores[i] += 1
        else:
            scores[i] -= 1

        # check if the player has been eliminated
        if scores[i] <= -10:
            eliminated[i] = True
            clear_output(wait=True)
            print(f"Player{i+1} has been eliminated with a score of {scores[i]}.")
            continue

    # create a list of remaining players and their scores
    remaining_scores = []
    remaining_players = []
    for i, score in enumerate(scores):
        if not eliminated[i]:
            remaining_scores.append(score)
            remaining_players.append(i+1)

    # clear the output area and print the updated scores for each player
    clear_output(wait=True)
    for i, score in enumerate(remaining_scores):
        print(f"Player{remaining_players[i]}: {score}", end="")
        if eliminated[remaining_players[i]-1]:
            print(" (eliminated)")
        else:
            print()
    time.sleep(1)

import torch
import time
from IPython.display import clear_output

# initialize the scores and elimination status for each player
scores = torch.zeros(4)
eliminated = torch.zeros(4, dtype=torch.bool)

while True:
    # check if any player has reached a score of 10
    if (scores == 10).any():
        winner = torch.argmax(scores)
        clear_output(wait=True)
        print(f"Player{winner+1} has won with a score of {scores[winner]}. Game over.")
        break

    # check if all but one player have been eliminated
    if (eliminated == False).sum() == 1:
        winner = torch.argmax(eliminated == False)
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

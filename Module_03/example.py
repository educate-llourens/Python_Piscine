#!/usr/bin/env python3

import sys

if __name__ == "__main__":
    player_scores: list = []
    i: int = 0

    if len(sys.argv) > 1:
        # try:
        #     player_scores.append(int(i))
        # except ValueError:
        print("Error: Invalid input.")
        for score in sys.argv:
            if score is type(int):
                player_scores.append(score)
            else:
                print(f"{score} must be a number")
    else:
        print("You did not enter any scores")

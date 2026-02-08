#!/usr/bin/env python3

import sys


def check_input() -> list[int]:
    scores_list: list = []

    for score in sys.argv[1:]:
        try:
            int(score)
        except ValueError:
            print(f"Error: {score} is not a number")
            continue
        scores_list.append(score)
    return scores_list


if __name__ == "__main__":
    if len(sys.argv) > 1:
        player_scores: list[int] = check_input()
        total_players: int = len(player_scores)
        total_score: int = sum(player_scores)
        try:
            average_score: float = total_score / total_players
        except ZeroDivisionError:
            pass
        high_score: int = max(player_scores)
        lowest_score: int = min(player_scores)
        range: int = high_score - lowest_score
    print("No scores provided. Usage: python3 ft_score_analytics.py "
          "<score1> <score2> ...")

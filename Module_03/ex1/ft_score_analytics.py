#!/usr/bin/env python3

import sys


def check_input() -> list[int]:
    int_list: list[int] = []
    score_int: int = 0

    for score in sys.argv[1:]:
        try:
            score_int = int(score)
            int_list.append(score_int)
        except ValueError:
            print(f"\033[31mError: {score} is not a number\033[0m\n")
            continue
    return int_list


def main() -> None:
    if len(sys.argv) > 1:
        try:
            player_scores: list[int] = check_input()
        except ValueError:
            return
        total_players: int = len(player_scores)
        total_score: int = sum(player_scores)
        average_score: float = total_score / total_players
        high_score: int = max(player_scores)
        lowest_score: int = min(player_scores)
        range: int = high_score - lowest_score

        print("=== Player Score Analytics ===")
        print(f"Scores processed: {player_scores}")
        print(f"Total players: {total_players}")
        print(f"Total score: {total_score}")
        print(f"Average score: {average_score}")
        print(f"High score: {high_score}")
        print(f"Low score: {lowest_score}")
        print(f"Score range: {range}")

    else:
        print("=== Player Score Analytics ===")
        print("No scores provided. Usage: python3 ft_score_analytics.py "
              "<score1> <score2> ...")


if __name__ == "__main__":
    main()

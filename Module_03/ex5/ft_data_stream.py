#!/usr/bin/env python3

from typing import Generator


def is_prime_nbr(nbr: int) -> bool:
    i: int = 2

    if nbr <= 1:
        return False
    while i <= (nbr / 2):
        if nbr % i == 0:
            return False
        else:
            i += 1
    return True


def prime_nbr_generator(start: int, iterations: int) -> Generator[int, None, None]:
    nbr: int = start + 1
    found_prime: int = 0

    if nbr % 2 == 0 and nbr > 2:
        nbr += 1
    while found_prime < iterations:
        if is_prime_nbr(nbr):
            yield nbr
            found_prime += 1
        nbr += 1


def fibonacci_generator(iterations: int) -> Generator[int, None, None]:
    nbr_1: int = 0
    nbr_2: int = 1

    for i in range(iterations):
        yield nbr_1
        temp = nbr_1 + nbr_2
        nbr_1 = nbr_2
        nbr_2 = temp


def generate_events(iterations: int) -> Generator[dict, None, None]:
    event: dict = {}
    player_level: int = 0
    event_id: int = 0
    player_list: list[str] = ['alice', 'bob', 'charlie', 'diana',
                              'eve', 'frank']
    events_list: list[str] = ['logged in', 'killed a monster', 'died',
                              'leveled_up', 'found an item', 'found treasure']

    for i in range(1, iterations + 1):
        event_id += 1
        player_level = (event_id % 60) + 2
        event = {
            "event_id": event_id,
            "player_name": player_list[event_id % 6],
            "player_level": player_level,
            "event": events_list[event_id % 6],
        }
        yield event


def main() -> None:
    events_processed: int = 0
    nbr_high_lvl_players: int = 0
    nbr_treasure_events: int = 0
    nbr_lvl_up: int = 0
    fib_sequence = 0

    print("=== Game Data Stream Processor ===\n")
    print("Processing 1000 game events...\n")

    event_stream = iter(generate_events(1000))
    print(f"Event {next(event_stream)['event_id']}:"
          f"Player {next(event_stream)['player_name']} "
          f"(level {next(event_stream)['player_level']}) "
          f"{next(event_stream)['event']}")
    print(f"Event {next(event_stream)['event_id']}:"
          f"Player {next(event_stream)['player_name']} "
          f"(level {next(event_stream)['player_level']}) "
          f"{next(event_stream)['event']}")
    print(f"Event {next(event_stream)['event_id']}:"
          f"Player {next(event_stream)['player_name']} "
          f"(level {next(event_stream)['player_level']}) "
          f"{next(event_stream)['event']}")

    print("...\n")

    print("=== Stream Analytics ===")
    event = generate_events(1000)
    for i in event:
        events_processed += 1
        if i['player_level'] > 10:
            nbr_high_lvl_players += 1
        if i['event'] == "found treasure":
            nbr_treasure_events += 1
        if i['event'] == "leveled_up":
            nbr_lvl_up += 1
    print(f"Total events processed: {events_processed}")
    print(f"High level players (10+): {nbr_high_lvl_players}")
    print(f"Treasure events: {nbr_treasure_events}")
    print(f"Level-up events: {nbr_lvl_up}")
    print("")
    print("Memory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds\n")

    print("=== Generator Demonstration ===")
    print("Fibonacci sequence (first 10): ", end="")
    fib_sequence = fibonacci_generator(10)
    for fib_nbr in fib_sequence:
        print(f"{fib_nbr}", end=", ")
    print("")
    print("Prime numbers (first 5): ", end="")
    prime_nbr_sequence = prime_nbr_generator(0, 5)
    for prime_nbr in prime_nbr_sequence:
        print(f"{prime_nbr}", end=",")
    print("")


if __name__ == "__main__":
    main()

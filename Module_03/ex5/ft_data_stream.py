#!/usr/bin/env python3

from typing import Generator


def generate_events(iterations: int) -> Generator[dict, None, None]:
    event: dict = {}
    player_level: int = 0
    event_id: int = 0
    player_list: list[str] = ['alice', 'bob', 'charlie', 'diana',
                              'eve', 'frank']
    events_list: list[str] = ['logged in', 'killed a monster', 'died',
                              'leveled_up', 'found an item']

    for i in range(1, iterations + 1):
        event_id += 1
        player_level = event_id % 10
        event = {
            "event_id": event_id,
            "player_name": player_list[event_id % 6],
            "player_level": player_level,
            "event": events_list[event_id % 5]
        }
        yield event


def main() -> None:
    event_1: dict = {}

    print("=== Game Data Stream Processor ===\n")
    print("Processing 1000 game events...\n")
    # event = generate_events(100)
    # event_1 = next(event)
    # print(f"Event {event_1["event_id"]}: Player {event_1["player_name"]} "
    #       f"(level {event_1["player_level"]}) {event_1["event"]}")
    # event_2 = next(event)
    # print(f"Event {event_2["event_id"]}: Player {event_2["player_name"]} "
    #       f"(level {event_2["player_level"]}) {event_2["event"]}")
    for i in range(3):
        event = generate_events(100)


if __name__ =="__main__":
    main()

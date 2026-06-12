import random
from typing import Generator, List, Tuple


class AdvancedDataHelper:
    """Advanced utilities for complex data scenarios."""

    def __init__(self) -> None:
        self.player_names: list[str] = [
            "Alice",
            "Bob",
            "Charlie",
            "Diana",
            "Eve",
            "Frank",
            "Grace",
            "Henry",
            "Ivy",
            "Jack",
            "Kate",
            "Liam",
            "Maya",
            "Noah",
            "Olivia",
            "Paul",
        ]

    def gen_event(self) -> Generator[Tuple[str, str]]:
        """Generate streaming game events for generator testing."""
        event_types = ["run", "eat", "grab", "swim", "move", "climb", "sleep"]

        while True:
            res: tuple[str, str] = (
                random.choice(self.player_names),
                random.choice(event_types),
            )
            yield res

    def consume_event(
        self, list_resourse: List[Tuple[str, str]]
    ) -> Generator[Tuple[str, str]]:
        while list_resourse:
            res: tuple[str, str] = list_resourse.pop(
                random.randint(0, len(list_resourse)) - 1
            )
            yield res


def main() -> None:

    print("=== Game Data Stream Processor ===\n")
    helper = AdvancedDataHelper()

    duration = 1000
    for i in range(duration):
        player: str
        event: str
        player, event = next(helper.gen_event())
        print(f" Event {i}: Player {player} did action {event}")

    list_tuple: list[Tuple[str, str]] = []
    duration = 10
    for i in range(duration):
        list_tuple.append(next(helper.gen_event()))

    print(f"Built a list of {duration} events {list_tuple}")
    for elem in helper.consume_event(list_tuple):
        print(f"Got event from list: {elem}")
        print(f"Remains in list: {list_tuple}")


if __name__ == "__main__":
    main()

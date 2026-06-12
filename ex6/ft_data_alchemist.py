import random
from typing import Generator, List


class AdvancedDataHelper:
    """Advanced utilities for complex data scenarios."""

    def __init__(self) -> None:
        self.player_names: list[str] = [
            "Alice",
            "bob",
            "Charlie",
            "dylan",
            "Emma",
            "Gregory",
            "john",
            "kevin",
            "Liam",
        ]

    def makecap(self) -> List[str]:
        return [name.capitalize() for name in self.player_names]

    def only_cap(self) -> List[str]:
        return [name for name in self.player_names
                if name == name.capitalize()]

    def gen_number(self) -> Generator[int]:
        while True:
            score: int = random.randint(0, 1000)
            yield score


def main() -> None:
    print("=== Game Data Alchemist ===\n")
    helper = AdvancedDataHelper()

    print(f"Initial list of players: {helper.player_names}")
    cap_names: List[str] = helper.makecap()
    print(f"New list with all names capitalized: {cap_names}")
    only_cap = helper.only_cap()
    print(f"New list of capitalized names only: {only_cap}")

    score_dict: dict[str, int] = {k: v for k, v in
                                  zip(cap_names, helper.gen_number())}

    mean_score: float = sum(score_dict.values()) / len(score_dict)
    print(f"Score dict: {score_dict}")
    print(f"Score average is {round(mean_score, 2)}")

    high_score_dict: dict[str, int] = {k: v for k, v in
                                       score_dict.items()
                                       if float(v) > mean_score}

    print(f"High scores: {high_score_dict}")


if __name__ == "__main__":
    main()

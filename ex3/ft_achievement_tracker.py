import random
from typing import Dict, List, Set


class AdvancedDataHelper:
    """Advanced utilities for complex data scenarios."""

    def __init__(self) -> None:
        self.player_names: List[str] = [
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

        self.achievements: List[str] = [
            "first_kill",
            "level_10",
            "level_50",
            "level_100",
            "speedrun",
            "explorer",
            "treasure_hunter",
            "boss_slayer",
            "collector",
            "perfectionist",
            "social_butterfly",
            "lone_wolf",
            "strategist",
            "berserker",
            "pacifist",
            "completionist",
        ]

        self.item_types = [
            "sword",
            "shield",
            "potion",
            "bow",
            "arrow",
            "armor",
            "helmet",
            "boots",
            "ring",
            "amulet",
            "scroll",
            "gem",
            "key",
            "map",
        ]

    def gen_player_achievements(self,
                                player_count: int = 20) -> Dict[str, Set[str]]:
        """Generate complex achievement networks with dependencies."""
        network: Dict[str, Set[str]] = {}

        for i in range(player_count):
            player: str = f"{self.player_names[i]}"

            # Simulate achievement progression
            player_achievements: set[str] = set()

            # Everyone gets basic achievements
            if random.random() > 0.1:  # 90% chance
                player_achievements.add("first_kill")

            if "first_kill" in player_achievements and random.random() > 0.3:
                player_achievements.add("level_10")

            if "level_10" in player_achievements and random.random() > 0.6:
                player_achievements.add("level_50")

            if "level_50" in player_achievements and random.random() > 0.8:
                player_achievements.add("level_100")

            # Add random achievements
            available: List[str] = [
                a for a in self.achievements if a not in player_achievements
            ]
            num_random: int = random.randint(0, min(5, len(available)))
            player_achievements.update(random.sample(available, num_random))

            network[player] = player_achievements

        return network


def unique_achievement(network: Dict[str, Set[str]]) -> Set[str]:
    return set.union(*network.values())


def shared_achievement(network: Dict[str, Set[str]]) -> Set[str]:
    return set.intersection(*network.values())


def achieve_player(network: Dict[str, Set[str]]) -> Dict[str, Set[str]]:
    res: Dict[str, Set[str]] = {}
    common_with_other: Set[str] = set()
    for main_player in network.keys():
        for player in network.keys():
            if player != main_player:
                inter: Set[str] = network[main_player].\
                    intersection(network[player])
                common_with_other = common_with_other.union(inter)
        res[main_player] = network[main_player].difference(common_with_other)
    return res


def missing_achieve_player(network:
                           Dict[str, Set[str]]) -> Dict[str, Set[str]]:
    res: Dict[str, Set[str]] = {}
    common_with_other: Set[str] = set()
    for main_player in network.keys():
        for player in network.keys():
            if player != main_player:
                inter: Set[str] = network[main_player].\
                    intersection(network[player])
                common_with_other = common_with_other.union(inter)
        res[main_player] = common_with_other.difference(network[main_player])
    return res


def main() -> None:
    print("=== Achievement Tracker System ===\n")
    helper = AdvancedDataHelper()
    network: Dict[str, Set[str]] = helper.gen_player_achievements(5)
    print("Achievement network:")
    for player, achievements in network.items():
        print(f"  {player}: {achievements}")
    print()
    print()
    print(f"All distinct achievements: {unique_achievement(network)}")
    print()
    print(f"Common achievements: {shared_achievement(network)}")
    print()
    print("Achievements unique per player :")
    achieve_unique_player: Dict[str, Set[str]] = achieve_player(network)
    for player, achievements in achieve_unique_player.items():
        print(f"Only {player} has : {achievements}")
    print()
    print()
    print("Missing achievements: ")
    missing_achieve: Dict[str, Set[str]] = missing_achieve_player(network)
    for player, achievements in missing_achieve.items():
        print(f"{player} is missing : {achievements}")
    print()


if __name__ == "__main__":
    main()

import itertools
import math

from solutions import BaseSolution


WEAPONS = [
    {"name": "Dagger", "cost": 8, "damage": 4, "armor": 0},
    {"name": "Shortsword", "cost": 10, "damage": 5, "armor": 0},
    {"name": "Warhammer", "cost": 25, "damage": 6, "armor": 0},
    {"name": "Longsword", "cost": 40, "damage": 7, "armor": 0},
    {"name": "Greataxe", "cost": 74, "damage": 8, "armor": 0},
]

ARMOR = [
    {"name": "Leather", "cost": 13, "damage": 0, "armor": 1},
    {"name": "Chainmail", "cost": 31, "damage": 0, "armor": 2},
    {"name": "Splitmail", "cost": 53, "damage": 0, "armor": 3},
    {"name": "Bandedmail", "cost": 75, "damage": 0, "armor": 4},
    {"name": "Platemail", "cost": 102, "damage": 0, "armor": 5},
]

RINGS = [
    {"name": "Damage +1", "cost": 25, "damage": 1, "armor": 0},
    {"name": "Damage +2", "cost": 50, "damage": 2, "armor": 0},
    {"name": "Damage +3", "cost": 100, "damage": 3, "armor": 0},
    {"name": "Defense +1", "cost": 20, "damage": 0, "armor": 1},
    {"name": "Defense +2", "cost": 40, "damage": 0, "armor": 2},
    {"name": "Defense +3", "cost": 80, "damage": 0, "armor": 3},
]


class Year2015Day21(BaseSolution):
    module_file = __file__

    def _parse_line(self, line: str):
        return int(line.strip().split(" ")[-1])

    def _parse_inputs(self):
        hp, damage, armor = super()._parse_inputs()
        return {"hp": hp, "damage": damage, "armor": armor}

    def get_stats(self, equipment):
        damage = 0
        armor = 0
        cost = 0

        for item in equipment:
            damage += item["damage"]
            armor += item["armor"]
            cost += item["cost"]

        return ({"hp": 100, "damage": damage, "armor": armor}, cost)

    def fight(self, player, boss):
        player_damage = player["damage"] - boss["armor"]
        boss_damage = boss["damage"] - player["armor"]

        player_turns_to_win = (
            math.ceil(boss["hp"] / player_damage) if player_damage > 0 else math.inf
        )
        boss_turns_to_win = (
            math.ceil(player["hp"] / boss_damage) if boss_damage > 0 else math.inf
        )

        winner = "player" if player_turns_to_win <= boss_turns_to_win else "boss"

        return winner

    def run_simulation(self, equipment, boss, results_costs):
        player, cost = self.get_stats(equipment)

        winner = self.fight(player, boss)
        if winner == "player":
            results_costs["win"].append(cost)
        else:
            results_costs["loss"].append(cost)

    def get_winning_costs(self):
        boss = self.inputs

        results_costs = {"win": [], "loss": []}

        ring_sets = []
        ring_sets.extend([ring] for ring in RINGS)
        ring_sets.extend(itertools.permutations(RINGS, 2))

        for weapon in WEAPONS:
            self.run_simulation([weapon], boss, results_costs)

            for ring_set in ring_sets:
                self.run_simulation([weapon, *ring_set], boss, results_costs)

            for armor in ARMOR:
                self.run_simulation([weapon, armor], boss, results_costs)

                for ring_set in ring_sets:
                    self.run_simulation([weapon, armor, *ring_set], boss, results_costs)

        return results_costs

    def part_1(self):
        return min(self.get_winning_costs()["win"])

    def part_2(self):
        return max(self.get_winning_costs()["loss"])


if __name__ == "__main__":
    Year2015Day21().print_results()

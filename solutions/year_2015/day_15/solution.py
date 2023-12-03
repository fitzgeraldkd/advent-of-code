from functools import reduce

from solutions import BaseSolution


class Year2015Day15(BaseSolution):
    module_file = __file__

    def _parse_line(self, line: str):
        name, properties = line.strip().split(": ")
        properties = {
            key: int(value)
            for key, value in [
                property.split(" ") for property in properties.split(", ")
            ]
        }
        return name, properties

    def _parse_inputs(self):
        ingredients = super()._parse_inputs()
        return {name: properties for name, properties in ingredients}

    def calculate_score(self, ingredients, amounts):
        totals = {"capacity": 0, "durability": 0, "flavor": 0, "texture": 0}

        for ingredient in ingredients.keys():
            for property in ["capacity", "durability", "flavor", "texture"]:
                totals[property] += (
                    ingredients[ingredient][property] * amounts[ingredient]
                )

        return reduce(lambda x, y: x * y, [max(value, 0) for value in totals.values()])

    def optimize_ingredient(self, ingredients, ingredient, amounts):
        previous_score = self.calculate_score(ingredients, amounts)

        for ingredient_to_remove in filter(
            lambda name: name != ingredient, ingredients.keys()
        ):
            while (
                self.calculate_score(ingredients, amounts) >= previous_score
                and amounts[ingredient_to_remove] > 1
            ):
                previous_score = self.calculate_score(ingredients, amounts)
                amounts[ingredient] += 1
                amounts[ingredient_to_remove] -= 1

            amounts[ingredient] -= 1
            amounts[ingredient_to_remove] += 1

        return amounts

    def get_calories(self, ingredients, amounts):
        return sum(
            [
                ingredients[ingredient]["calories"] * amounts[ingredient]
                for ingredient in ingredients.keys()
            ]
        )

    def part_1(self):
        ingredients = self.inputs
        ingredient_names = list(ingredients.keys())
        amounts = {}

        for ingredient in ingredient_names[:-1]:
            amounts[ingredient] = 100 // len(ingredients)
        amounts[ingredient_names[-1]] = 100 - sum(amounts.values())

        previous_score = 0

        while self.calculate_score(ingredients, amounts) > previous_score:
            previous_score = self.calculate_score(ingredients, amounts)
            for ingredient in ingredients.keys():
                amounts = self.optimize_ingredient(ingredients, ingredient, amounts)

        return self.calculate_score(ingredients, amounts)

    def part_2(self):
        ingredients = self.inputs
        amounts = {}

        best_score = 0

        ingredient_names = list(ingredients.keys())

        # Assumes 4 ingredients.
        for i in range(97):
            x = i + 1
            amounts[ingredient_names[0]] = x
            for j in range(97 - x):
                y = j + 1
                amounts[ingredient_names[1]] = y
                for k in range(97 - x - y):
                    z = k + 1
                    amounts[ingredient_names[2]] = z
                    amounts[ingredient_names[3]] = 100 - x - y - z
                    if self.get_calories(ingredients, amounts) == 500:
                        best_score = max(
                            best_score, self.calculate_score(ingredients, amounts)
                        )

        return best_score


if __name__ == "__main__":
    Year2015Day15().print_results()

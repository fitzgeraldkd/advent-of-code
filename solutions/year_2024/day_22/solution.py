from collections import defaultdict

from solutions import BaseSolution


class Year2024Day22(BaseSolution):
    module_file = __file__

    def _parse_line(self, line):
        return int(super()._parse_line(line))

    def mix(self, secret_number: int, operand: int):
        return secret_number ^ operand

    def prune(self, secret_number: int):
        return secret_number % 16777216

    def generate_next_secret_number(self, secret_number: int):
        secret_number = self.mix(secret_number, secret_number * 64)
        secret_number = self.prune(secret_number)

        secret_number = self.mix(secret_number, secret_number // 32)
        secret_number = self.prune(secret_number)

        secret_number = self.mix(secret_number, secret_number * 2048)
        secret_number = self.prune(secret_number)

        return secret_number

    def get_price(self, secret_number: int):
        return secret_number % 10

    def part_1(self):
        results = 0

        for secret_number in self.inputs:
            for _ in range(2000):
                secret_number = self.generate_next_secret_number(secret_number)
            results += secret_number

        return results

    def part_2(self):
        results = defaultdict(int)

        for secret_number in self.inputs:
            checked_spots = set()
            current_sequence = tuple()
            old_price = self.get_price(secret_number)
            for _ in range(2000):
                new_secret_number = self.generate_next_secret_number(secret_number)
                new_price = self.get_price(new_secret_number)
                delta = new_price - old_price
                if len(current_sequence) < 4:
                    current_sequence = (*current_sequence, delta)
                else:
                    current_sequence = (*current_sequence[1:4], delta)

                if len(current_sequence) == 4 and current_sequence not in checked_spots:
                    checked_spots.add(current_sequence)
                    results[current_sequence] += new_price

                secret_number = new_secret_number
                old_price = new_price

        max_price = 0
        for price in results.values():
            max_price = max(price, max_price)

        return max_price


if __name__ == "__main__":
    Year2024Day22().print_results()

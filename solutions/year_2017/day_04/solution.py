from solutions import BaseSolution


class Year2017Day04(BaseSolution):
    module_file = __file__

    def _parse_line(self, line):
        return super()._parse_line(line).split(" ")

    def part_1(self):
        passphrases = self.inputs
        valid_count = 0

        for passphrase in passphrases:
            if len(passphrase) == len(set(passphrase)):
                valid_count += 1

        return valid_count

    def part_2(self):
        passphrases = self.inputs
        valid_count = 0

        for passphrase in passphrases:
            passphrase = [''.join(sorted(word)) for word in passphrase]
            if len(passphrase) == len(set(passphrase)):
                valid_count += 1

        return valid_count


if __name__ == "__main__":
    Year2017Day04().print_results()

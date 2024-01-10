from solutions import BaseSolution


class Year2016Day20(BaseSolution):
    module_file = __file__

    MAX_ADDRESS = 4294967295

    def _parse_line(self, line: str):
        return [int(address) for address in line.strip().split("-")]

    def part_1(self):
        blacklist = self.inputs
        address = 0
        changed_address = True

        while changed_address:
            changed_address = False
            for start, end in blacklist:
                if start <= address and end >= address:
                    changed_address = True
                    address = end + 1
                    break

        return address

    def part_2(self):
        blacklist = self.inputs
        whitelist_count = 0
        address = 0

        while address <= self.MAX_ADDRESS:
            blacklisted = False
            for start, end in blacklist:
                if start <= address and end >= address:
                    blacklisted = True
                    address = end + 1
                    break
            if not blacklisted:
                whitelist_count += 1
                address += 1

        return whitelist_count


if __name__ == "__main__":
    Year2016Day20().print_results()

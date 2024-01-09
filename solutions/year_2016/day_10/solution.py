from solutions import BaseSolution


class Year2016Day10(BaseSolution):
    module_file = __file__

    TARGETS = [17, 61]

    def give_value(
        self, bots: dict, outputs: dict, recipient, value: int, targets=None
    ):
        if recipient[0] == "output":
            outputs[recipient[1]] = value
        elif recipient[1] in bots:
            bots[recipient[1]]["values"].append(value)
            if len(bots[recipient[1]]["values"]) == 2:
                values = bots[recipient[1]]["values"]
                bots[recipient[1]]["values"] = []
                if targets and set(targets) == set(values):
                    return recipient[1]
                winner = self.give_value(
                    bots, outputs, bots[recipient[1]]["low"], min(values), targets
                )
                if winner is not None:
                    return winner
                winner = self.give_value(
                    bots, outputs, bots[recipient[1]]["high"], max(values), targets
                )
                if winner is not None:
                    return winner
        else:
            bots[recipient[1]] = {"values": [value], "low": None, "high": None}

    def part_1(self):
        instructions = self.inputs

        bots = {}
        outputs = {}

        for instruction in instructions:
            if not instruction.startswith("value"):
                (
                    _,
                    bot,
                    _,
                    _,
                    _,
                    low_type,
                    low_bot,
                    _,
                    _,
                    _,
                    high_type,
                    high_bot,
                ) = instruction.split(" ")
                bot, low_bot, high_bot = int(bot), int(low_bot), int(high_bot)
                low = (low_type, low_bot)
                high = (high_type, high_bot)
                if bot in bots:
                    bots[bot]["low"] = low
                    bots[bot]["high"] = high
                else:
                    bots[bot] = {"values": [], "low": low, "high": high}

        for instruction in instructions:
            if instruction.startswith("value"):
                _, value, _, _, _, recipient = instruction.split(" ")
                value, recipient = int(value), ("bot", int(recipient))
                winner = self.give_value(bots, outputs, recipient, value, self.TARGETS)

        return winner

    def part_2(self):
        instructions = self.inputs

        bots = {}
        outputs = {}

        for instruction in instructions:
            if not instruction.startswith("value"):
                (
                    _,
                    bot,
                    _,
                    _,
                    _,
                    low_type,
                    low_bot,
                    _,
                    _,
                    _,
                    high_type,
                    high_bot,
                ) = instruction.split(" ")
                bot, low_bot, high_bot = int(bot), int(low_bot), int(high_bot)
                low = (low_type, low_bot)
                high = (high_type, high_bot)
                if bot in bots:
                    bots[bot]["low"] = low
                    bots[bot]["high"] = high
                else:
                    bots[bot] = {"values": [], "low": low, "high": high}

        for instruction in instructions:
            if instruction.startswith("value"):
                _, value, _, _, _, recipient = instruction.split(" ")
                value, recipient = int(value), ("bot", int(recipient))
                self.give_value(bots, outputs, recipient, value)

        return outputs[0] * outputs[1] * outputs[2]


if __name__ == "__main__":
    Year2016Day10().print_results()

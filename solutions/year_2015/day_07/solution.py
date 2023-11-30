from solutions import BaseSolution


TARGET_WIRE = "a"


def get_value(wires, label, calculated_wires):
    if label in calculated_wires:
        return calculated_wires[label]

    wire = wires[label]

    def read_input(wires, input):
        try:
            return int(input)
        except ValueError:
            return get_value(wires, input, calculated_wires)

    inputs = [read_input(wires, input) for input in wire["inputs"]]

    if wire["action"] == "AND":
        value = inputs[0] & inputs[1]
    elif wire["action"] == "ASSIGN":
        value = inputs[0]
    elif wire["action"] == "LSHIFT":
        value = inputs[0] << inputs[1]
    elif wire["action"] == "NOT":
        value = ~inputs[0]
    elif wire["action"] == "OR":
        value = inputs[0] | inputs[1]
    elif wire["action"] == "RSHIFT":
        value = inputs[0] >> inputs[1]

    value %= 65536

    calculated_wires[label] = value
    return value


class Year2015Day07(BaseSolution):
    def _parse_line(self, line: str):
        split_input = line.strip().split(" -> ")

        action = None
        for action_to_split in ["AND", "LSHIFT", "OR", "RSHIFT"]:
            if action_to_split in split_input[0]:
                action = action_to_split
                values = split_input[0].split(f" {action} ")

        if "NOT" in split_input[0]:
            action = "NOT"
            values = [split_input[0][4:]]

        if action is None:
            action = "ASSIGN"
            values = [split_input[0]]

        return {"action": action, "destination": split_input[1], "values": values}

    def _parse_inputs(self):
        lines = super()._parse_inputs()
        return {
            line["destination"]: {
                "action": line["action"],
                "inputs": line["values"],
            }
            for line in lines
        }

    def part_1(self):
        return get_value(self.inputs, TARGET_WIRE, {})

    def part_2(self):
        wires = self.inputs
        wires["b"] = {"action": "ASSIGN", "inputs": [self.part_1()]}
        return get_value(wires, TARGET_WIRE, {})


if __name__ == "__main__":
    Year2015Day07(__file__).print_results()

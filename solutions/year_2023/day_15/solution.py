from collections import defaultdict, OrderedDict

from solutions import BaseSolution


class Year2023Day15(BaseSolution):
    module_file = __file__

    def _parse_inputs(self):
        return super()._parse_inputs()[0].split(",")

    def get_hash(self, label: str) -> int:
        value = 0
        for char in label:
            value += ord(char)
            value *= 17
            value %= 256
        return value

    def part_1(self):
        return sum(self.get_hash(label) for label in self.inputs)

    def part_2(self):
        boxes = defaultdict(OrderedDict)

        for step in self.inputs:
            label, action, focal_length = None, None, None
            if "-" in step:
                label = step[:-1]
                action = "-"
            else:
                label, focal_length = step.split("=")
                focal_length = int(focal_length)
                action = "="

            box_id = self.get_hash(label)

            if action == "=":
                boxes[box_id][label] = focal_length
            elif label in boxes[box_id]:
                del boxes[box_id][label]

        total = 0
        for box_index, box in boxes.items():
            for slot_index, focal_length in enumerate(box.values()):
                total += (box_index + 1) * (slot_index + 1) * focal_length

        return total


if __name__ == "__main__":
    Year2023Day15().print_results()

import re
from collections import defaultdict
from datetime import datetime

from solutions import BaseSolution


class Year2018Day04(BaseSolution):
    module_file = __file__

    def _parse_line(self, line: str):
        stripped_line = line.strip()
        return datetime.fromisoformat(stripped_line[1:17]), stripped_line[19:]

    def _parse_inputs(self):
        records = [self._parse_line(line) for line in self._read_inputs()]
        records.sort(key=lambda record: record[0])

        active_guard = None
        sleep_counts = defaultdict(lambda: defaultdict(int))
        sleep_minute = None

        for record in records:
            if "#" in record[1]:
                active_guard = int(re.search(r"\#[0-9]+", record[1]).group(0)[1:])
                sleep_minute = None
            elif record[1] == "falls asleep":
                sleep_minute = record[0].minute
            else:
                for minute in range(sleep_minute, record[0].minute):
                    sleep_counts[active_guard][minute] += 1
                sleep_minute = None

        return sleep_counts

    def part_1(self):
        sleep_counts = self.inputs

        sleepiest_guard = max(
            sleep_counts.items(), key=lambda sleep_count: sum(sleep_count[1].values())
        )
        sleepiest_minute = max(
            sleepiest_guard[1].items(), key=lambda minutes: minutes[1]
        )[0]

        return sleepiest_guard[0] * sleepiest_minute

    def part_2(self):
        sleep_counts = self.inputs

        sleepiest_guard = max(
            sleep_counts.items(), key=lambda sleep_count: max(sleep_count[1].values())
        )
        sleepiest_minute = max(
            sleepiest_guard[1].items(), key=lambda minutes: minutes[1]
        )[0]

        return sleepiest_guard[0] * sleepiest_minute


if __name__ == "__main__":
    Year2018Day04().print_results()

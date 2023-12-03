from solutions import BaseSolution


class Year2015Day14(BaseSolution):
    RACE_DURATION = 2503
    module_file = __file__

    def _parse_line(self, line: str):
        name, _, _, speed, _, _, duration, *_, rest, _ = line.split(" ")

        return {
            "name": name,
            "speed": int(speed),
            "duration": int(duration),
            "rest": int(rest),
        }

    def get_distance(self, reindeer, time):
        cycle_duration = reindeer["duration"] + reindeer["rest"]
        cycle_distance = reindeer["speed"] * reindeer["duration"]
        full_cycles = time // cycle_duration
        additional_time = time % cycle_duration
        additional_distance = (
            min(additional_time, reindeer["duration"]) * reindeer["speed"]
        )
        return (cycle_distance * full_cycles) + additional_distance

    def is_resting(self, reindeer, time):
        cycle_duration = reindeer["duration"] + reindeer["rest"]
        time_in_cycle = time % cycle_duration
        return time_in_cycle >= reindeer["duration"]

    def part_1(self):
        distances = [
            self.get_distance(reindeer, self.RACE_DURATION) for reindeer in self.inputs
        ]

        return max(distances)

    def part_2(self):
        inputs = self.inputs

        point_map = {}
        position_map = {}
        for reindeer in inputs:
            point_map[reindeer["name"]] = 0
            position_map[reindeer["name"]] = 0

        for time in range(self.RACE_DURATION):
            for reindeer in inputs:
                if not self.is_resting(reindeer, time):
                    position_map[reindeer["name"]] += reindeer["speed"]

            leading_distance = 0
            leading_reindeer = []
            for reindeer in inputs:
                distance = position_map[reindeer["name"]]
                if distance == leading_distance:
                    leading_reindeer.append(reindeer["name"])
                elif distance > leading_distance:
                    leading_distance = distance
                    leading_reindeer = [reindeer["name"]]

            for reindeer in leading_reindeer:
                point_map[reindeer] += 1

        return max(point_map.values())


if __name__ == "__main__":
    Year2015Day14().print_results()

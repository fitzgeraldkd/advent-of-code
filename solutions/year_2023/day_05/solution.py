import math

from solutions import BaseSolution


class Year2023Day05(BaseSolution):
    group_delimiter = "\n"
    module_file = __file__

    def _parse_inputs(self):
        seeds, *maps = super()._parse_inputs()
        parsed_seeds = [int(s) for s in seeds[0].split(": ")[-1].split(" ")]
        parsed_maps = [[[int(v) for v in l.split(" ")] for l in m[1:]] for m in maps]
        return parsed_seeds, parsed_maps

    def part_1(self):
        seeds, maps = self.inputs

        min_location = math.inf
        for seed in seeds:
            current = seed
            for map in maps:
                for destination, source, length in map:
                    if source <= current < source + length:
                        current += destination - source
                        break

            min_location = min(min_location, current)

        return min_location

    def part_2(self):
        seeds, maps = self.inputs

        seed_ranges = []
        for i in range(0, len(seeds), 2):
            seed_ranges.append([seeds[i], seeds[i + 1]])

        min_location = math.inf
        for start_seed, seed_length in seed_ranges:
            current_seed = start_seed

            while current_seed < start_seed + seed_length:
                current_value = current_seed
                possible_adders = []

                for map in maps:
                    match_found = False

                    # If the current value mathes one of the lines in the map, determine
                    # the value where that line would no longer be matched.
                    for destination, source, length in map:
                        if source <= current_value < source + length:
                            possible_adders.append(source + length - current_value)
                            current_value += destination - source
                            match_found = True
                            break

                    # If the current value doesn't match any of the lines in the map,
                    # determine the value where the next line would apply.
                    if not match_found:
                        possible_sources = [
                            source for _, source, _ in map if source > current_value
                        ]
                        if possible_sources:
                            possible_adders.append(
                                min(possible_sources) - current_value
                            )

                min_location = min(min_location, current_value)

                # After all the maps have been processed, determine the next index that
                # would cause a different line in the map to be used.
                if possible_adders:
                    current_seed += max(min(possible_adders), 1)
                else:
                    current_seed += 1

        return min_location


if __name__ == "__main__":
    Year2023Day05().print_results()

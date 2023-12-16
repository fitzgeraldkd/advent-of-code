from copy import deepcopy
from collections import defaultdict
import itertools
import regex as re

from solutions import BaseSolution


class Year2023Day12(BaseSolution):
    module_file = __file__

    def _parse_line(self, line: str):
        springs, groups = line.strip().split(' ')
        groups = [int(group) for group in re.findall(r'\d+', groups)]
        return springs, groups

    # def _parse_inputs(self):
    #     return super()._parse_inputs()[0]

    def get_possibilities(self, springs: str, sub_springs, remaining_groups, group_maps):

        # Efficiency ideas:
        # - If there are n known consecutive '#' cells, and n is the max number possible, then change the adjacent cells to be '.'

        # TODO: Next attempt: bucket all groups into sections, separated by known inactive geysers. For each combination of buckets:
        # - Identify the number of permutations within each bucket
        # - Multiply these together to get the total for that combination
        # Then add all those products together for the grand total of possibilities

        # TODO: Next step: deep copy group_maps, pop items as they are used since they can't be needed in deeper iterations.
        # group_maps = deepcopy(group_maps)


        # print(indeces)
        # print(sub_springs)
        # print(group_maps)
        start_index = len(springs) - len(sub_springs)

        required_length = sum(remaining_groups) + len(remaining_groups) - 1

        if len(sub_springs) < required_length:
            return 0

        next_group = remaining_groups[0]
        # print(remaining_groups)
        if len(remaining_groups) > 1:
            possibilities = 0
            # print(sub_springs, remaining_groups)
            # print(sub_springs[remaining_groups[0] + 1])
            # return get_possibilities(springs, sub_springs[remaining_groups[0] + 1], remaining_groups[1:], group_maps)

            # print(group_maps[next_group])


            # TODO: Toggle this depending on if testing deep copy (memory may be an issue).
            for i in group_maps[next_group]:
            # while group_maps[next_group]:
                # i = group_maps[next_group].pop(0)



                # print(possibilities, springs, i, required_length, next_group, indeces, remaining_groups)
                # if len(springs) - i < required_length - next_group - 1:
                #     break
                if '#' in springs[start_index:i]:
                    break
                if i < start_index:
                    continue
                if len(springs) - i < required_length:
                    break
                if springs[i + next_group] == '#':
                    continue
                # possibilities += get_possibilities(springs, sub_springs[i - start_index + next_group + 1:], remaining_groups[1:], group_maps)
                possibilities += self.get_possibilities(springs, springs[i + next_group + 1:], remaining_groups[1:], group_maps)

            return possibilities
        else:
            # print(springs[start_index:i])
            # print(indeces)
            return len({i for i in group_maps[next_group] if ((i >= start_index) and ('#' not in springs[start_index:i]) and ('#' not in sub_springs or sub_springs.index('#') >= i - start_index))})


    def part_1(self):
        # possibilities = 0

        # for springs, groups in self.inputs:

        #     group_maps = defaultdict(set)
        #     # print(springs)
        #     for group_size in groups:
        #         # print(group_size)
        #         # for match in re.finditer(fr'(^|\?|\.)[\?\#]{{{group_size}}}($|\?|\.)', springs, overlapped=True):
        #         #     print(match)
        #         #     group_maps[group_size].add(match.start())
        #         for match in re.finditer(fr'^[\?\#]{{{group_size}}}($|\?|\.)', springs, overlapped=True):
        #             group_maps[group_size].add(match.start())
        #         for match in re.finditer(fr'(\?|\.)[\?\#]{{{group_size}}}($|\?|\.)', springs, overlapped=True):
        #             group_maps[group_size].add(match.start() + 1)

        #     sorted_group_maps = {}
        #     for size in groups:
        #         sorted_group_maps[size] = sorted(group_maps[size])
        #     # print(group_maps.items())
        #     # for key, groups in group_maps.items():
        #     #     pass
        #     #     sorted_group_maps[int(key)] = sorted(groups)

        #     # print(group_maps)
        #     # print(sorted_group_maps)

        #     possibilities += self.get_possibilities(springs, springs, groups, sorted_group_maps)

        # return possibilities

        ####################

        possibilities = 0

        for springs, groups in self.inputs:
            pattern = r'\.+'.join([fr'\#{{{l}}}' for l in groups])

            operational = {i for i, char in enumerate(springs) if char == '.'}
            damaged = {i for i, char in enumerate(springs) if char == '#'}
            unknown = {i for i, char in enumerate(springs) if char == '?'}

            total_damaged = sum(groups)
            number_missing = total_damaged - len(damaged)
            # print(springs, groups, number_missing)
            combinations = itertools.combinations(unknown, number_missing)
            for combination in combinations:
                test_springs = ['.' if char == '?' else char for char in springs]
                for i in combination:
                    test_springs[i] = '#'

                if re.search(pattern, ''.join(test_springs)):
                    # print(''.join(test_springs))
                    possibilities += 1

        return possibilities

    def part_2(self):
        # possibilities = 0

        # for springs, groups in self.inputs:
        #     print(possibilities)
        #     springs = '?'.join([springs for _ in range(5)])
        #     groups = groups * 5

        #     pattern = r'\.+'.join([fr'\#{{{l}}}' for l in groups])

        #     damaged = springs.count('#')
        #     unknown = {i for i, char in enumerate(springs) if char == '?'}

        #     total_damaged = sum(groups)
        #     number_missing = total_damaged - damaged
        #     # print(springs, groups, number_missing)
        #     combinations = itertools.combinations(unknown, number_missing)
        #     for combination in combinations:
        #         test_springs = ['.' if char == '?' else char for char in springs]
        #         for i in combination:
        #             test_springs[i] = '#'

        #         if re.search(pattern, ''.join(test_springs)):
        #             # print(''.join(test_springs))
        #             possibilities += 1


        # return possibilities


        ###################################

        possibilities = 0

        for springs, groups in self.inputs:
            springs = '?'.join([springs for _ in range(5)])
            groups = groups * 5

            group_maps = defaultdict(set)
            # print(springs)
            for group_size in groups:
                # print(group_size)
                # for match in re.finditer(fr'(^|\?|\.)[\?\#]{{{group_size}}}($|\?|\.)', springs, overlapped=True):
                #     print(match)
                #     group_maps[group_size].add(match.start())
                for match in re.finditer(fr'^[\?\#]{{{group_size}}}($|\?|\.)', springs, overlapped=True):
                    group_maps[group_size].add(match.start())
                for match in re.finditer(fr'(\?|\.)[\?\#]{{{group_size}}}($|\?|\.)', springs, overlapped=True):
                    group_maps[group_size].add(match.start() + 1)

            sorted_group_maps = {}
            for size in groups:
                sorted_group_maps[size] = sorted(group_maps[size])
            # print(group_maps.items())
            # for key, groups in group_maps.items():
            #     pass
            #     sorted_group_maps[int(key)] = sorted(groups)

            # print(group_maps)
            # print(sorted_group_maps)

            possibilities += self.get_possibilities(springs, springs, groups, sorted_group_maps)
            print(possibilities)

            continue

            pattern = r'[\?\.]+'.join([fr'[#\?]{{{l}}}' for l in groups])
            min_length = sum(groups) + len(groups) - 1
            for i in range(len(springs) - min_length + 1):
                if re.match(pattern, springs[i:]):
                    possibilities += 1

            print(springs, groups, possibilities)
            print(pattern)

            continue



            # print(springs)
            pattern = r'[\?\.]+'.join([fr'[#\?]{{{l}}}' for l in groups])
            # print(pattern)
            # print(re.findall(pattern, springs))
            matches = re.findall(pattern, springs)
            print(springs, matches)
            # matches = re.findall(fr'(?=({pattern}))', springs)
            # print(fr'(?=({pattern}))')
            possibilities += len(list(matches))


            continue

            # SLOW ROUTE

            springs = '?'.join([springs for _ in range(5)])
            groups = groups * 5
            print(possibilities, springs, groups)

            pattern = r'\.+'.join([fr'\#{{{l}}}' for l in groups])

            # operational = {i for i, char in enumerate(springs) if char == '.'}
            # damaged = {i for i, char in enumerate(springs) if char == '#'}
            damaged = springs.count('#')
            unknown = {i for i, char in enumerate(springs) if char == '?'}

            # print(re.findall(fr'#{{{max(groups)}}}', springs))
            # for match in re.findall(fr'#{{{max(groups)}}}', springs):
            #     print(match.__dict__)

            total_damaged = sum(groups)
            number_missing = total_damaged - (damaged)
            # print(springs, groups, number_missing)
            combinations = itertools.combinations(unknown, number_missing)
            for combination in combinations:
                test_springs = ['.' if char == '?' else char for char in springs]
                for i in combination:
                    test_springs[i] = '#'

                if re.search(pattern, ''.join(test_springs)):
                    # print(''.join(test_springs))
                    possibilities += 1

        return possibilities


if __name__ == "__main__":
    print('Sample:')
    Year2023Day12('sample.txt').print_results()
    print('Actual:')
    Year2023Day12().print_results()

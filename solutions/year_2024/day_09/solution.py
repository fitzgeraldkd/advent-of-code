from solutions import BaseSolution


class Year2024Day09(BaseSolution):
    module_file = __file__

    def _parse_inputs(self):
        return super()._parse_inputs()[0]

    def part_1(self):
        disk_map = self.inputs
        disk_map = [int(v) for v in disk_map]

        results = []
        length_type = "file"
        file_index = 0
        for size in disk_map:
            if length_type == "file":
                results.extend([file_index for _ in range(size)])
                file_index += 1
                length_type = "free"
            else:
                results.extend([None for _ in range(size)])
                length_type = "file"

        a, b = 0, len(results) - 1
        while a < b:
            if results[a] is None:
                while results[b] is None:
                    b -= 1
                results[a] = results[b]
                results[b] = None
            a += 1

        results = [v for v in results if v is not None]

        return sum([i * v for i, v in enumerate(results)])

    def part_2(self):
        """
        To improve:
        The empty spaces can be filled as the results are being created. Check from the
        end of the input to see if they can plugged in.
        """
        disk_map = self.inputs
        disk_map = [int(v) for v in disk_map]

        results = []
        length_type = "file"
        file_index = 0
        for size in disk_map:
            if length_type == "file":
                results.extend([file_index for _ in range(size)])
                file_index += 1
                length_type = "free"
            else:
                results.extend([None for _ in range(size)])
                length_type = "file"

        file_index = results[-1]
        end_index = len(results) - 1
        while file_index > 0:
            # print()
            # # print(results)
            # foo = [("." if v is None else f"{v}") for v in results]
            # print("".join(foo))
            # print(len(results))
            # print("Checking", file_index)
            start_index = end_index
            while results[start_index - 1] == file_index:
                start_index -= 1
            length = end_index - start_index + 1

            blank_index = 0
            while blank_index <= len(results) - length:
                if blank_index > end_index:
                    break

                if results[blank_index] is not None:
                    blank_index += 1
                    continue

                values_to_check = results[blank_index:blank_index+length]
                # print(values_to_check)
                if all([v is None for v in values_to_check]):
                    for i in range(blank_index, blank_index + length):
                        results[i] = file_index
                    for i in range(start_index, end_index + 1):
                        results[i] = None
                    break
                blank_index += 1

            file_index -= 1
            while results[end_index] != file_index:
                end_index -= 1
        # a, b = 0, len(results) - 1
        # while a < b:
        #     if results[a] is None:
        #         while results[b] is None:
        #             b -= 1
        #         results[a] = results[b]
        #         results[b] = None
        #     a += 1

        # results = [v for v in results if v is not None]

        return sum([i * v for i, v in enumerate(results) if v is not None])


if __name__ == "__main__":
    Year2024Day09().print_results()

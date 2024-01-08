from solutions import BaseSolution


class Year2016Day04(BaseSolution):
    module_file = __file__

    def _parse_line(self, line: str):
        split_input = line.strip()[:-1].split("-")
        room_name = " ".join(split_input[:-1])
        sector_id, checksum = split_input[-1].split("[")
        return room_name, int(sector_id), checksum

    def count_letters(self, room_name):
        letter_sum = {}
        for letter in room_name:
            if letter == " ":
                continue
            if letter in letter_sum:
                letter_sum[letter] += 1
            else:
                letter_sum[letter] = 1
        return letter_sum

    def get_checksum(self, room_name):
        counted_letters = self.count_letters(room_name)
        letters = sorted(
            sorted(counted_letters.keys()),
            key=lambda letter: counted_letters[letter],
            reverse=True,
        )

        return "".join(letters[:5])

    def decrypt_room_name(self, room_name, sector_id):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        decrypted = []
        for letter in room_name:
            if letter == " ":
                decrypted.append(" ")
                continue
            decrypted.append(alphabet[(alphabet.index(letter) + sector_id) % 26])
        return "".join(decrypted)

    def part_1(self):
        inputs = self.inputs

        total = 0
        for room_name, sector_id, checksum in inputs:
            if checksum == self.get_checksum(room_name):
                total += sector_id

        return total

    def part_2(self):
        inputs = self.inputs

        for room_name, sector_id, checksum in inputs:
            if checksum == self.get_checksum(room_name):
                if (
                    self.decrypt_room_name(room_name, sector_id)
                    == "northpole object storage"
                ):
                    return sector_id

        return None


if __name__ == "__main__":
    Year2016Day04().print_results()

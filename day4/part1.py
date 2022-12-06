from typing import List


def convert_id_range_to_range(id_range: str) -> List[int]:
    # Input type: X-Y and returns a range from [x, Y]
    x, y = id_range.split("-")
    return list(range(int(x), int(y) + 1))


with open("data.txt", "r", newline="\n") as input_data:

    overlapping_schedules = 0
    for entry in input_data.readlines():
        entry = entry.strip()
        first_turn, second_turn = entry.split(",")

        first_turn = convert_id_range_to_range(first_turn)
        second_turn = convert_id_range_to_range(second_turn)

        if set(first_turn).issuperset(set(second_turn)):
            overlapping_schedules += 1
        elif set(second_turn).issuperset(set(first_turn)):
            overlapping_schedules += 1

    print(overlapping_schedules)

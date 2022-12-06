ASCII_LOWER_A_VALUE = 97 - 1  # To start from 1, 2, 3 .. 26
ASCII_UPPER_A_VALUE = 65 - 1  # To start from 1, 2, 3 .. 26
UPPER_CASE_START_VALUE = 26  # Upper case letters value starts from 27

with open("data.txt", "r", newline="\n") as input_data:

    rucksacks = []
    common_items = []
    for idx, entry in enumerate(input_data.readlines(), start=1):
        entry = entry.strip()

        if idx % 3 == 0:
            rucksacks.append(list(entry))
            common_items += list(set(rucksacks[0]).intersection(set(rucksacks[1]), set(rucksacks[2])))
            rucksacks = []
        else:
            rucksacks.append(list(entry))

    print(
        sum(
            [
                ord(item) - ASCII_UPPER_A_VALUE + UPPER_CASE_START_VALUE
                if item.isupper()
                else ord(item) - ASCII_LOWER_A_VALUE
                for item in common_items
            ]
        )
    )

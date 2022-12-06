ASCII_LOWER_A_VALUE = 97 - 1  # To start from 1, 2, 3 .. 26
ASCII_UPPER_A_VALUE = 65 - 1  # To start from 1, 2, 3 .. 26
UPPER_CASE_START_VALUE = 26  # Upper case letters value starts from 27

with open("data.txt", "r", newline="\n") as input_data:

    common_items = []
    for entry in input_data.readlines():
        entry = entry.strip()

        num_items = len(entry)
        first_compartment = list(entry[: num_items // 2])
        second_compartment = list(entry[num_items // 2 :])

        common_items += list(
            set(first_compartment).intersection(set(second_compartment))
        )

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

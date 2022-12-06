# Part one
# ===========================
with open("data.txt", "r", newline="\n") as input_data:
    max_calories = 0
    elf_calories = 0
    for entry in input_data.readlines():
        if entry == "\r\n":
            max_calories = max(elf_calories, max_calories)
            elf_calories = 0
        else:
            elf_calories += int(entry)

    print(f"Part 1: {max(elf_calories, max_calories)}")

# Part two
# ===========================
with open("data.txt", "r", newline="\n") as input_data:
    elves_calories = []
    elf_calories = 0
    for entry in input_data.readlines():
        if entry == "\r\n":
            elves_calories.append(elf_calories)
            elf_calories = 0
        else:
            elf_calories += int(entry)
    elves_calories.append(elf_calories)

    elves_calories.sort()

    print(f"Part 2: {sum(elves_calories[-3:])}")

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

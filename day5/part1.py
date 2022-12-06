from collections import deque

with open("data.txt", "r", newline="\n") as input_data:

    warehouse = {}
    boxes = []
    for entry in input_data.readlines():
        if "[" in entry and "]" in entry:
            entry = list(entry.removesuffix("\r\n"))
            boxes.append([entry[idx] for idx in range(1, len(entry), 4)])

        elif entry.startswith(" 1"):
            for box_letters in reversed(boxes):
                for stack_idx, box_letter in enumerate(box_letters, start=1):
                    if box_letter == " ":
                        continue

                    stack = warehouse.get(stack_idx, deque())
                    stack.append(box_letter)
                    warehouse[stack_idx] = stack

        elif entry.startswith("move"):
            order = entry.split(" ")
            quantity = int(order[1])
            origin = int(order[3])
            destination = int(order[5])

            for _ in range(quantity):
                box_letter = warehouse[origin].pop()
                warehouse[destination].append(box_letter)

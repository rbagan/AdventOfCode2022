from enum import Enum


class Shape(str, Enum):
    A = "ROCK"
    B = "PAPER"
    C = "SCISSORS"
    X = "ROCK"
    Y = "PAPER"
    Z = "SCISSORS"


class ShapeValue(int, Enum):
    A = 1
    B = 2
    C = 3
    X = 1
    Y = 2
    Z = 3


RockPaperScissors = {
    ("PAPER", "PAPER"): 3,
    ("PAPER", "ROCK"): 0,
    ("PAPER", "SCISSORS"): 6,
    ("ROCK", "PAPER"): 6,
    ("ROCK", "ROCK"): 3,
    ("ROCK", "SCISSORS"): 0,
    ("SCISSORS", "PAPER"): 0,
    ("SCISSORS", "ROCK"): 6,
    ("SCISSORS", "SCISSORS"): 3,
}

with open("data.txt", "r", newline="\n") as input_data:
    score = 0
    for entry in input_data.readlines():
        opponent_play, my_play = [x.strip() for x in entry.split(" ")]
        score += (
            RockPaperScissors[(Shape[opponent_play], Shape[my_play])]
            + ShapeValue[my_play]
        )

    print(score)

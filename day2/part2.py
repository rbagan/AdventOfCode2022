from enum import Enum


class Shape(str, Enum):
    A = "ROCK"
    B = "PAPER"
    C = "SCISSORS"


class ShapeValue(int, Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


class RoundPrediction(str, Enum):
    X = "LOSE"
    Y = "DRAW"
    Z = "WIN"


RoundPredictionShape = {
    ("PAPER", "WIN"): Shape.C,
    ("PAPER", "LOSE"): Shape.A,
    ("PAPER", "DRAW"): Shape.B,
    ("ROCK", "WIN"): Shape.B,
    ("ROCK", "LOSE"): Shape.C,
    ("ROCK", "DRAW"): Shape.A,
    ("SCISSORS", "WIN"): Shape.A,
    ("SCISSORS", "LOSE"): Shape.B,
    ("SCISSORS", "DRAW"): Shape.C,
}

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
        opponent_choise, my_choise = [x.strip() for x in entry.split(" ")]

        my_choise = RoundPredictionShape[
            (Shape[opponent_choise], RoundPrediction[my_choise])
        ].value

        score += (
            RockPaperScissors[(Shape[opponent_choise], my_choise)]
            + ShapeValue[my_choise]
        )

    print(score)

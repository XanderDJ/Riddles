from enum import Enum
from random import choice


class Color(Enum):
    RED = 1
    BLUE = 3
    PURPLE = 2


def mix(c1: Color, c2: Color):
    if c1 == Color.BLUE and c2 == Color.RED or c2 == Color.BLUE and c1 == Color.RED:
        return Color.PURPLE
    elif c1 == Color.BLUE and c2 == Color.PURPLE or c2 == Color.BLUE and c1 == Color.PURPLE:
        return Color.RED
    else:
        return Color.BLUE


class Game:
    def __init__(self, blue: int, red: int, purple: int):
        self.blue = blue
        self.red = red
        self.purple = purple

    def get_total(self):
        return self.blue + self.red + self.purple

    def get_amount(self, color: Color):
        if color == Color.BLUE:
            return self.blue
        elif color == Color.RED:
            return self.red
        else:
            return self.purple

    def take(self, color: Color):
        if color == Color.BLUE:
            self.blue -= 1
        elif color == Color.RED:
            self.red -= 1
        else:
            self.purple -= 1

    def add(self, color: Color):
        if color == Color.BLUE:
            self.blue += 1
        elif color == Color.RED:
            self.red += 1
        else:
            self.purple += 1

    def colors_to_mix(self):
        blue = (self.blue, Color.BLUE)
        red = (self.red, Color.RED)
        purple = (self.purple, Color.PURPLE)
        lst = [blue, red, purple]
        lst.sort(key=lambda x: x[0])
        highest = lst[2]
        if lst[1][0] > lst[0][0]:
            second = lst[1]
        else:
            second = choice(lst[:2])
        return highest[1], second[1]

    def step(self):
        c1, c2 = self.colors_to_mix()
        self.take(c1)
        self.take(c2)
        self.add(mix(c1, c2))

    def play(self):
        while self.get_total() != 1:
            self.step()
        return self.blue, self.red, self.purple


game = Game(24, 43, 33)
tup = game.play()
print(tup)

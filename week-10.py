from random import randint
from sys import argv


class Die:
    def __init__(self, num, sides):
        self.num = num
        self.sides = sides

    def roll(self) -> int:
        return randint(1, self.sides)


if __name__ == "__main__":
    sides, numOfDice, rolls = 6, 1, 1

    if "-s" in argv:
        sides = int(argv[argv.index("-s") + 1])
    if "-n" in argv:
        numOfDice = int(argv[argv.index("-n") + 1])
    if "-r" in argv:
        rolls = int(argv[argv.index("-r") + 1])

    dice = [Die(i + 1, sides) for i in range(numOfDice)]

    for i in range(rolls):
        print(f"----Roll: {i + 1}/{rolls}----")
        for die in dice:
            print(f"Die {die.num}: {die.roll()}")

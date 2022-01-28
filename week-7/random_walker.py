from turtle import Turtle, Screen, mode
import random

WINDOW_SIZE = {
    "width": 800,
    "height": 800
}


def check_bounds(direction, stepSize):
    x, y = turtle.pos()
    match direction:
        case 0:  # up
            return False if y + stepSize > WINDOW_SIZE["height"]/2 else True
        case 1:  # down
            return False if y - stepSize < -WINDOW_SIZE["height"]/2 else True
        case 2:  # west
            return False if x - stepSize < -WINDOW_SIZE["width"]/2 else True
        case 3:  # east
            return False if x + stepSize > WINDOW_SIZE["width"]/2 else True


def set_direction(direction):
    match direction:
        case 0:  # up
            turtle.setheading(0)
        case 1:  # down
            turtle.setheading(180)
        case 2:  # west
            turtle.setheading(270)
        case 3:  # east
            turtle.setheading(90)


def main(steps=10):
    for i in range(steps):
        stepSize = random.randint(10, 100)
        direction = random.randint(0, 3)
        check = check_bounds(direction, stepSize)
        while not check:
            direction = random.randint(0, 3)
            check = check_bounds(direction, stepSize)
        set_direction(direction)
        turtle.forward(stepSize)


if __name__ == '__main__':
    # screen & turtle set up
    turtle = Turtle()
    mode('logo')
    screen = Screen()
    screen.setup(WINDOW_SIZE["width"], WINDOW_SIZE["height"])

    # main loop
    turtle.speed(0)
    main(200)

    screen.listen()
    screen.mainloop()

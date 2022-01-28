import turtle

t = turtle.Turtle()


def draw_polygon(side_length, sides):
    for i in range(sides):
        t.forward(side_length)
        t.right(360 / sides)

    turtle.done()

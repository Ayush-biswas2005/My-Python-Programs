import turtle


def draw_circle(color, radius, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()


def draw_line(color, x1, y1, x2, y2):
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.color(color)
    turtle.goto(x2, y2)


def draw_bike():
    turtle.speed(1)

    # Draw wheels
    draw_circle("black", 50, -100, -50)
    draw_circle("black", 50, 100, -50)

    # Draw frame
    draw_line("blue", -100, -50, -30, 50)
    draw_line("blue", 100, -50, 30, 50)
    draw_line("blue", -30, 50, 30, 50)
    draw_line("blue", 0, 0, -100, -50)
    draw_line("blue", 0, 0, 100, -50)

    # Draw handlebars
    draw_line("blue", 30, 50, 60, 90)
    draw_line("blue", 60, 90, 90, 90)

    # Draw seat
    draw_line("blue", -30, 50, -30, 80)
    draw_line("blue", -30, 80, 0, 80)

    turtle.hideturtle()
    turtle.done()


# Call the function to draw the bike
draw_bike()


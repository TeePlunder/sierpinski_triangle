import turtle

# triangle configurations
triangle_edge_counter = 3
triangle_width = 300
triangle_angle = 120

turtle.speed(2)

triangle_positions = [turtle.pos(), (0.0, 0.0), (0.0, 0.0)]

# DRAW BASIC TRIANGLE
for i in range(triangle_edge_counter):
    triangle_positions[i] = turtle.pos()
    turtle.forward(triangle_width)
    turtle.left(triangle_angle)


def draw_triangle(division):
    for i in range(triangle_edge_counter):
        triangle_positions[i] = turtle.pos()
        turtle.forward(triangle_width / division)
        turtle.right(triangle_angle)


def goto_new_position(position):
    turtle.penup()
    turtle.goto(position)
    turtle.pendown()


def get_midpoint(point1_index, point2_index):
    point1_position = triangle_positions[point1_index]
    point2_position = triangle_positions[point2_index]
    x1 = point1_position[0]
    x2 = point2_position[0]
    y1 = point1_position[1]
    y2 = point2_position[1]
    return (x1 + x2) / 2, (y1 + y2) / 2


# ((x1+x2)/2, (y1+y2)/2)
goto_new_position(get_midpoint(0, 2))

division = 2
# for i in range(1):
#     if i > 0:
#         division = division * 2
draw_triangle(division)

goto_new_position((-15, -15))
turtle.seth(180)
for i in range(triangle_edge_counter):
    turtle.forward(triangle_width / division)
    turtle.left(triangle_angle)

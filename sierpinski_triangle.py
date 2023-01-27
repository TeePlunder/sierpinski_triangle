import turtle

# triangle configurations
triangle_edge_counter = 3
triangle_width = 300
triangle_angle = 120

turtle.speed(5)


def goto_new_position(position):
    turtle.penup()
    turtle.goto(position)
    turtle.pendown()


def get_midpoint(positions, point1_index, point2_index):
    point1_position = positions[point1_index]
    point2_position = positions[point2_index]
    x1 = point1_position[0]
    x2 = point2_position[0]
    y1 = point1_position[1]
    y2 = point2_position[1]
    return (x1 + x2) / 2, (y1 + y2) / 2


def draw_triangle_direction_right(division):
    triangle_position = []
    turtle.seth(0)
    for i in range(triangle_edge_counter):
        triangle_position.append(turtle.pos())
        turtle.forward(triangle_width / division)
        turtle.right(triangle_angle)
    return triangle_position


def draw_triangle_direction_left(division):
    triangle_position = []
    turtle.seth(180)
    for i in range(triangle_edge_counter):
        triangle_position.append(turtle.pos())
        turtle.forward(triangle_width / division)
        turtle.left(triangle_angle)
    return triangle_position


def draw_triangle_direction_top(division):
    triangle_position = []
    turtle.seth(triangle_angle / 2)
    for i in range(triangle_edge_counter):
        triangle_position.append(turtle.pos())
        turtle.forward(triangle_width / division)
        turtle.left(triangle_angle)
    return triangle_position


def draw_triangles(to_draw, division_nr):
    new_drawn_queue = []
    for positions in to_draw:
        goto_new_position(get_midpoint(positions, 0, 2))
        new_drawn_queue.append(draw_triangle_direction_left(division_nr))

        goto_new_position(get_midpoint(positions, 0, 1))
        new_drawn_queue.append(draw_triangle_direction_top(division_nr))

        goto_new_position(get_midpoint(positions, 1, 2))
        new_drawn_queue.append(draw_triangle_direction_right(division_nr))
    return new_drawn_queue


# DRAW BASIC TRIANGLE
first_positions = []
to_draw_list = []

for i in range(triangle_edge_counter):
    first_positions.append(turtle.pos())
    turtle.forward(triangle_width)
    turtle.left(triangle_angle)
to_draw_list.append(first_positions)

# DRAW SECOND TRIANGLE
division = 2
nList = []
for p in to_draw_list:
    goto_new_position(get_midpoint(p, 0, 2))
    nList.append(draw_triangle_direction_right(division))

# START AUTO GENERATING
to_draw_list = nList

division = division * 2
to_draw_list = draw_triangles(to_draw_list, division)

division = division * 2
to_draw_list = draw_triangles(to_draw_list, division)

import turtle

import triangle

# triangle configurations
triangle_edge_counter = 3
triangle_width = 600
triangle_angle = 120


def goto_new_position(position):
    turtle.penup()
    turtle.goto(position)
    turtle.pendown()


def get_midpoint(position_1, position_2):
    x1 = position_1[0]
    x2 = position_2[0]
    y1 = position_1[1]
    y2 = position_2[1]
    return (x1 + x2) / 2, (y1 + y2) / 2


def create_new_triangle(drawn_edge, positions):
    position_a = positions[0]
    position_b = positions[1]
    position_c = positions[2]
    midpoint_ab = get_midpoint(position_a, position_b)
    midpoint_ac = get_midpoint(position_a, position_c)
    midpoint_bc = get_midpoint(position_b, position_c)

    return triangle.Triangle(drawn_edge, position_a, position_b, position_c, midpoint_ab, midpoint_ac, midpoint_bc)


def draw_triangle_in_direction_right(division):
    triangle_position = []
    turtle.seth(0)
    for i in range(triangle_edge_counter):
        triangle_position.append(turtle.pos())
        turtle.forward(triangle_width / division)
        turtle.right(triangle_angle)
    return create_new_triangle("right", triangle_position)


def draw_triangle_in_direction_left(division):
    triangle_position = []
    turtle.seth(180)
    for i in range(triangle_edge_counter):
        triangle_position.append(turtle.pos())
        turtle.forward(triangle_width / division)
        turtle.left(triangle_angle)
    return create_new_triangle("left", triangle_position)


def draw_triangle_in_direction_top(division):
    triangle_position = []
    turtle.seth(triangle_angle / 2)
    for i in range(triangle_edge_counter):
        triangle_position.append(turtle.pos())
        turtle.forward(triangle_width / division)
        turtle.left(triangle_angle)
    return create_new_triangle("top", triangle_position)


def draw_triangles(to_draw, division_nr):
    new_drawn_queue = []
    for triangle in to_draw:
        match triangle.drawn_edge:
            case "right":
                goto_new_position(triangle.midpoint_ac)
                new_drawn_queue.append(draw_triangle_in_direction_left(division_nr))

                goto_new_position(triangle.midpoint_bc)
                new_drawn_queue.append(draw_triangle_in_direction_right(division_nr))

                goto_new_position(triangle.midpoint_ab)
                new_drawn_queue.append(draw_triangle_in_direction_top(division_nr))
            case "left":
                goto_new_position(triangle.midpoint_bc)
                new_drawn_queue.append(draw_triangle_in_direction_left(division_nr))

                goto_new_position(triangle.midpoint_ac)
                new_drawn_queue.append(draw_triangle_in_direction_right(division_nr))

                goto_new_position(triangle.midpoint_ab)
                new_drawn_queue.append(draw_triangle_in_direction_top(division_nr))
            case "top":
                goto_new_position(triangle.midpoint_ac)
                new_drawn_queue.append(draw_triangle_in_direction_left(division_nr))

                goto_new_position(triangle.midpoint_ab)
                new_drawn_queue.append(draw_triangle_in_direction_right(division_nr))

                goto_new_position(triangle.midpoint_bc)
                new_drawn_queue.append(draw_triangle_in_direction_top(division_nr))

    return new_drawn_queue


# TURTLE CONFIGURATIONS
turtle.speed(12)
goto_new_position((-300, -300))

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
second_triangle = []
for p in to_draw_list:
    goto_new_position(get_midpoint(p[0], p[2]))
    second_triangle.append(draw_triangle_in_direction_right(division))

# START AUTO GENERATING
to_draw_list = second_triangle

for i in range(4):
    division = division * 2
    to_draw_list = draw_triangles(to_draw_list, division)

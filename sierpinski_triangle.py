import turtle as turtle

# triangle configurations
triangleEdgeCounter = 3
triangleWidth = 300
triangleAngle = 120


def drawbasictriangle():
    for i in range(triangleEdgeCounter):
        turtle.forward(triangleWidth)
        turtle.left(triangleAngle)


drawbasictriangle()

for i in range(4):
    division = 2
    if i > 0:
        division = division * 2
    print(division)
    turtle.left(triangleAngle / 2)
    turtle.forward(triangleWidth / division)
    turtle.right(triangleAngle / 2)
    for j in range(triangleEdgeCounter):
        turtle.forward(triangleWidth / division)
        turtle.right(triangleAngle)
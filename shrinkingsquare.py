import turtle

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("light blue")
turtle_screen.title("Turtle Python")

turtle_instance = turtle.Turtle()
turtle_instance.color("red")

def shrinkiingSquare(size):
    for i in range(4):
        turtle_instance.forward(size)
        turtle_instance.left(90)
        size = size -5
shrinkiingSquare(150)
shrinkiingSquare(130)
shrinkiingSquare(110)
shrinkiingSquare(90)
shrinkiingSquare(70)
shrinkiingSquare(50)
shrinkiingSquare(30)
shrinkiingSquare(10)
turtle.done()
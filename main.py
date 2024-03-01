import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("Python Turtle")
turtle_instance = turtle.Turtle()
turtle_instance_2 = turtle.Turtle()
'''
turtle_instance.forward(20)
turtle_instance.left(90)
turtle_instance.forward(20)
turtle_instance.left(90)
turtle_instance.forward(20)
turtle_instance.left(90)
turtle_instance.forward(20)
'''
for i in range(5):
    turtle_instance.right(144)
    turtle_instance.forward(150)



turtle.done()
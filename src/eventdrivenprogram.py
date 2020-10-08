import turtle

#Create Window
wn=turtle.screensize(400,400,"yellow")
wn=turtle.Screen()
wn.title("Event Driven Programming")

#create turtle
tess = turtle.Turtle()

#Event actions
def up():
    tess.forward(30)


def left():
    tess.left(45)


def right():
    tess.right(45)

def quit():
    wn.bye()

#Events
wn.onkey(up, "Up")
wn.onkey(left, "Left")
wn.onkey(right, "Right")
wn.onkey(quit, "q")


wn.listen()
wn.mainloop()


import turtle
#Function to draw a bar

def drawbar (self, height):
    self.begin_fill()
    self.left(90)
    self.forward(height)
    self.write("   "+str(height))
    self.right(90)
    self.forward(40)
    self.right(90)
    self.forward(height)
    self.left(90)
    self.end_fill()
    self.penup()
    self.forward(10)
    self.pendown()

wn=turtle.Screen()
wn.bgcolor("yellow")
wn.title("Bar Chart")

t= turtle.Turtle()
t.penup()
t.back(200)

xs = [10, 20, 5, 40, 50]

for x in xs:
    drawbar(t, x)

wn.mainloop()

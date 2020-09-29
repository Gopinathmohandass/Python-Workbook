import turtle

#define the square function
def draw_quare(self,side):
    for i in range(4):
        self.forward(side)
        self.right(90)

#Create canvas
wn = turtle.Screen()

#Set Canvas attributes
wn.bgcolor("Yellow")
wn.title("Drawing Board")

#Create Turtle
alex = turtle.Turtle()
alex.pensize(10)

#Call the square function
draw_quare(alex,100)

wn.mainloop()


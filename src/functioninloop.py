import turtle

def draw_multicolor_squares(self,side):
    for i in range(4):
        self.forward(side)
        self.left(90)

wn=turtle.Screen()
wn.bgcolor("lightblue")
wn.title("Multi Color Squares")

alex = turtle.Turtle()
alex.pensize(3)
size = 5
colors = ("black", "yellow", "blue", "red", "green", "orange")

for i in range(25):
    alex.pencolor(colors[i%6])
    draw_multicolor_squares(alex,size)
    size += 5
    alex.forward(40)
    alex.left(20)

wn.mainloop()
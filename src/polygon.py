import turtle

def draw_polygon(self, side, len):
    angle = 360 / side
    for i in range(side):
        self.forward(len)
        self.left(angle)

wn = turtle.Screen()
tess = turtle.Turtle()
draw_polygon(tess,8,100)
wn.mainloop()
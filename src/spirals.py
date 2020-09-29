import turtle

def draw_spiral(self, len, angle):
    pattern = 360 // angle
    dl = 1
    for i in range(20):
        for j in range(pattern):
            self.forward(len+dl)
            self.left(angle)
            dl += 3

wn = turtle.Screen()
tess = turtle.Turtle()
draw_spiral(tess,1,90)
wn.mainloop()
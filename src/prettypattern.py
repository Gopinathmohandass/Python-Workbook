import turtle

def draw_pattern(self, len, angle):
    pattern = 360 // angle
    for i in range(20):
        for j in range(pattern):
            self.forward(len)
            self.left(angle)
        self.left(18)
wn = turtle.Screen()
tess = turtle.Turtle()
draw_pattern(tess,100,120)
wn.mainloop()
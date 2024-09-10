import turtle as trtl

screen = trtl.Screen()
screen.setup(width=800, height=800)

trtl = trtl.Turtle()
trtl.speed(0)

size = 20
size_increment = 20

while True:
    trtl.penup()
    trtl.goto(-size / 2, -size / 2)
    trtl.pendown()
    for _ in range(4):
        trtl.forward(size)
        trtl.left(90)
    size += size_increment
  
screen.mainloop()

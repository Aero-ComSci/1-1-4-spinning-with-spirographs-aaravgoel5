import turtle as trtl

screen = trtl.Screen()
screen.setup(width=800, height=800)

trtl = trtl.Turtle()
trtl.speed(0)

colors = ['red', 'green', 'blue', 'black', 'orange']
num = ['1','2', '3','4']

size = 20
size_incrm = 20
incrm = 0

for x in colors:  
    trtl.penup()
    trtl.goto(-size / 2, -size / 2)
    trtl.pendown()
    trtl.color(colors[incrm % len(colors)]) 
    j = 0
    for x in num:  
        trtl.forward(size)
        trtl.left(90)
        j += 1
    size += size_incrm 
    incrm += 1
    
screen.mainloop()

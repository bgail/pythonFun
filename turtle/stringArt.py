import turtle
t = turtle.Pen()
turtle.bgcolor('#021128')
t.speed(0)
t.pensize(1)
colors = ['blueviolet', 'cornflowerblue', 'darkgreen', 'maroon']
for x in range(300):
   t.pencolor( colors[x % 4] )
   t.circle(x)
   t.left(91)

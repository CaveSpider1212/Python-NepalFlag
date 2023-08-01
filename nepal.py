import turtle as t

# Turtle speed
t.speed("fast")

# Setup for border
t.penup()
t.color("#003893")
t.width(9)
t.goto(-100, -50)
t.left(90)
t.pendown()

# Border and inside
t.fillcolor("#DC143C")
t.begin_fill()
t.forward(250)
t.right(125)
t.forward(200)
t.right(145)
t.forward(115)
t.left(130)
t.forward(177.5)
t.right(130)
t.forward(160)
t.end_fill()
t.penup()

# Setup for moon (white circle)
t.goto(-35, 125)
t.color("white")
t.right(90)
t.width(1)
t.pendown()

# Moon (white circle)
t.fillcolor("white")
t.begin_fill()
t.circle(25)
t.end_fill()
t.penup()

# Setup for moon (red circle)
t.goto(-35, 132.5)
t.color("#DC143C")
t.pendown()

# Moon (red circle...used to make the crescent)
t.fillcolor("#DC143C")
t.begin_fill()
t.circle(25)
t.end_fill()
t.penup()

# Setup for sun on moon
t.goto(-78, 110)
t.color("white")
t.right(55)
t.width(1)
t.pendown()

# Sun on crescent moon
t.fillcolor("white")
t.begin_fill()
t.forward(5)
t.left(97.5)
for n in range(8):
    t.forward(6)
    t.right(135)
    t.forward(6)
    t.left(116)
t.right(40)
t.forward(5)
t.right(35)
t.forward(4)
t.right(90)
t.forward(30)
t.end_fill()
t.right(90)
t.penup()

# Setup for sun
t.goto(-70, 30)
t.left(10)
t.pendown()

# Sun
t.fillcolor("white")
t.begin_fill()
for n in range(12):
    t.forward(12.5)
    t.right(135)
    t.forward(12.5)
    t.left(105)
t.end_fill()
t.penup()

# Leaves window open when finished
t.exitonclick()
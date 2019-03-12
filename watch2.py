#watch2 is different only in seconds hand than the watch 1
import time
import turtle

wn=turtle.Screen()
wn.bgcolor('black')
wn.setup(600,600)
wn.tracer(0)

#pen 
pen=turtle.Turtle()
pen.hideturtle()


def draw_clock(pen,h,m,s):
    pen.color('blue')
    pen.penup()
    pen.setheading(90)
    pen.goto(120,0)
    pen.pensize(3)
    pen.pendown()
    pen.circle(120)
    pen.penup()
    pen.goto(130,0)
    pen.pendown()
    pen.circle(130)
    

    

    #draw 12 ticks
    for i in range(12):
        pen.color('yellow')
        pen.penup()
        pen.goto(0,0)
        pen.forward(100)
        pen.pendown()
        pen.forward(20)
        pen.right(30)
        
    #draw hour hand
    pen.penup()
    pen.pensize(3)
    pen.goto(0,0)
    pen.setheading(90)
    pen.color('white')
    angle=((h/12)*360)+(m/60)*30
    pen.right(angle)
    pen.pendown()
    pen.forward(60)
    
    #draw min hand
    pen.penup()
    pen.pensize(2)
    pen.goto(0,0)
    pen.setheading(90)
    pen.color('green')
    angle=((m/60)*360)+(s/60)*6
    pen.right(angle)
    pen.pendown()
    pen.forward(70)
    
    #draw sec hand
    
    pen.penup()
    pen.color('red')
    pen.shape('circle')
    pen.turtlesize(stretch_wid=0.4,stretch_len=0.4)
    pen.showturtle()
    pen.width(3)
    pen.setheading(90)
    pen.goto(0,0)
    angle=(s/60)*360
    pen.right(angle)
    pen.forward(130)
    pen.pendown()
    

    

i=1
while True:
    
    h=int(time.strftime("%H"))
    m=int(time.strftime("%M"))
    s=int(time.strftime("%S"))
    draw_clock(pen,h,m,s)#order is important draw,update,sleep and then clear
    wn.update()
    time.sleep(1)
    pen.clear()
    



wn.mainloop()

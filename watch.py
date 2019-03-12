import time
import turtle

wn=turtle.Screen()
wn.bgcolor('black')
wn.setup(600,600)
wn.tracer(0)

#pen 
pen=turtle.Turtle()
pen.hideturtle()

i=1
def draw_clock(pen,h,m,s):
    
    pen.color('green')
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
        pen.color('white')
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
    pen.color('blue')
    angle=((m/60)*360)+(s/60)*6
    pen.right(angle)
    pen.pendown()
    pen.forward(70)
    
    #draw sec hand
    pen.penup()
    pen.pensize(1)
    pen.goto(0,0)
    pen.setheading(90)
    pen.color('yellow')
    angle=(s/60)*360
    pen.right(angle)
    pen.pendown()
    pen.forward(80)
    

def pendulum(pen,i):
    #building pendulum case
    pen.penup()
    pen.showturtle()
    pen.shape('circle')
    pen.color('white')
    pen.width(2)
    pen.goto(0,0)
    pen.setheading(270-10*i)
    pen.forward(130)
    pen.pendown()
    pen.forward(120)

while True:
    
    h=int(time.strftime("%H"))
    m=int(time.strftime("%M"))
    s=int(time.strftime("%S"))
    
    draw_clock(pen,h,m,s)#order is important draw,update,sleep and then clear
    pendulum(pen,i)
    i=i*-1
    wn.update()
    time.sleep(1)
    #sleep for 1 sec for 2 sec time period of pendulum
    #sleepe for 0.5 sec for 1 sec of time period of pendulum
    pen.clear()
    
wn.mainloop()

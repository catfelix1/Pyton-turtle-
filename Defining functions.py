import turtle

turtle.speed(10)
x = 0
y = 0
x1 = 0
y1 = 250
counter = 0
screen = turtle.Screen()
screen.bgcolor("black")
def curlingice(x1, y1):
    turtle.goto(x1, y1)
    turtle.seth(0)
    turtle.pencolor("black")
    turtle.fillcolor("white")
    turtle.begin_fill()
    turtle.pendown()   
    turtle.right(0)
    turtle.fd(400)
    turtle.left(90)
    turtle.fd(200)
    turtle.left(90)
    turtle.fd(800)
    turtle.left(90)
    turtle.fd(200)
    turtle.left(90)
    turtle.fd(400)
    turtle.end_fill() 

def curlingline(x1 , y1):
    turtle.penup()
    turtle.goto(x1,y1+100)
    turtle.pencolor('black')
    turtle.back(400)
    turtle.pendown()
    turtle.fd(800)
    turtle.right(180)
    turtle.fd(32)
    turtle.right(90)
    turtle.fd(16)
    turtle.back(32)
    turtle.fd(8)
    turtle.left(90)
    turtle.fd(8)
    turtle.right(90)
    turtle.fd(16)
    turtle.right(90)
    turtle.fd(8)
    turtle.right(180)
    turtle.fd(738)
    turtle.right(90)
    turtle.fd(8)
    turtle.back(32)
    turtle.fd(8)
    turtle.right(90)
    turtle.fd(8)
    turtle.left(90)
    turtle.fd(16)
    turtle.back(16)
    turtle.right(90)
    turtle.fd(722)
    turtle.right(180)
    turtle.fd(32)
    turtle.right(90)
    turtle.fd(108)
    turtle.back(200)
    turtle.fd(100)
    turtle.left(90)
    turtle.fd(672)
    turtle.right(90)
    turtle.fd(100)
    turtle.back(200)
    turtle.fd(100)
    turtle.right(90)
    turtle.fd(60)
    turtle.right(90)
    turtle.fd(100)
    turtle.back(200)
    turtle.fd(100)
    turtle.left(90)
    turtle.fd(552)
    turtle.right(90)
    turtle.fd(100)
    turtle.back(200)
    turtle.fd(100)
    turtle.right(90)
    turtle.fd(200)
    turtle.right(90)
    turtle.fd(100)
    turtle.back(200)
    turtle.fd(100)
    turtle.left(90)
    turtle.fd(352)
    turtle.right(180)
    turtle.fd(200)
    turtle.left(90)
    turtle.fd(100)
    turtle.back(200)
    turtle.fd(100)
    turtle.left(90)
    turtle.fd(140)
   
    



def curlinghouse():
    turtle.pencolor('blue')
    turtle.fillcolor('blue')
    turtle.penup()
    turtle.left(270)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(60)
    turtle.end_fill()
    turtle.left(90)
    turtle.fd(20)
    turtle.right(90)
    turtle.pencolor('white')
    turtle.fillcolor('white')
    turtle.begin_fill()
    turtle.circle(40)
    turtle.left(90)
    turtle.fd(20)
    turtle.right(90)
    turtle.end_fill()
    turtle.pencolor('red')
    turtle.fillcolor('red')
    turtle.begin_fill()
    turtle.circle(20)
    turtle.end_fill()
    turtle.left(90)
    turtle.fd(10)
    turtle.right(90)
    turtle.end_fill()
    turtle.pencolor('white')
    turtle.fillcolor('white')
    turtle.begin_fill()
    turtle.circle(10)
    turtle.end_fill()
    turtle.penup()
    turtle.right(90)
    turtle.fd(643)
    turtle.back(41)
    turtle.pendown()
    turtle.left(180)



def curling(x, y):
    turtle.pu()
    turtle.goto(0, y1)
    turtle.pd()
    curlingice(x1, y1)
    curlingline(x1, y1)
    curlinghouse()
    curlinghouse()
while counter != 4:
    print("Curling is the best sport created.")
    counter = counter + 1
    
    for curlingrink in range(4):
    
        curling(x, y)
    
        y1 = y1 - 230
    
    
   
    


    

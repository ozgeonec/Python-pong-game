import turtle
#wn for window

wn=turtle.Screen()
wn.title("Pong by @ozgeonec")
wn.bgcolor("pink")
wn.setup(width=800, height=600)
wn.tracer(0) #stops the window from updating

# Paddle A
paddle_a = turtle.Turtle()#Turtle for class name
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("black")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B

paddle_b = turtle.Turtle()#Turtle for class name
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("black")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

#Ball
ball = turtle.Turtle()#Turtle for class name
ball.speed(0)
ball.shape("square")
ball.color("black")
ball.penup()
ball.goto(0, 0)

#Function

#ycornet method from turtle

def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

#Keyboard binding

wn.listen()  #listen to keyboard
wn.onkeypress(paddle_a_up(), "w")  #when press w call fun paddleaup
wn.onkeypress(paddle_a_down(), "s")

wn.onkeypress(paddle_b_up(), "Up")
wn.onkeypress(paddle_b_down(), "Down")


#Main game loop

while True:
    wn.update()


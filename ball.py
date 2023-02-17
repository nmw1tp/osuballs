import turtle
import random

window = turtle.Screen()

border = turtle.Turtle()
border.speed(5)
border.up()
border.hideturtle()
border.pensize(10)
border.color("green")
border.goto(300,300)
border.down()
border.goto(300,-300)
border.goto(-300,-300)
border.goto(-300,300)
border.goto(300,300)

window.tracer(2)
window.update()


balls=[]
count = 20
for i in range(count):
    ball = turtle.Turtle()
    ball.shape('circle')
    ball.up()
    randx = random.randint(-290,290)
    randy = random.randint(-290,290)
    red = random.random()
    green = random.random()
    blue = random.random()
    ball.color(red,green,blue)
    ball.hideturtle()
    ball.goto(randx,randy)
    ball.showturtle()
    dx = 30
    dy = 20
    balls.append([ball,dx,dy])

while True:
    for i in range(count):
        balls[i]
        x,y = balls[i][0].position()
        if x+balls[i][1] >= 300 or x+balls[i][1] <-300:
            balls[i][1]=-balls[i][1]
        if y+balls[i][2] >= 300 or y+balls[i][2] <-300:
            balls[i][2]=-balls[i][2]
        balls[i][0].goto(x+balls[i][1],y+balls[i][2])

window.mainloop()

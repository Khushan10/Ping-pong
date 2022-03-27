import turtle
playerA_score = 0
playerB_score = 0

window = turtle.Screen()
window.title("Ping-Pong Game")
window.bgcolor("black")
window.setup(width = 800, height = 600)
window.tracer(0)

#left paddle
leftPaddle = turtle.Turtle()
leftPaddle.speed(0)
leftPaddle.shape("square")
leftPaddle.color("green")
leftPaddle.shapesize(stretch_wid = 5, stretch_len = 1)
leftPaddle.penup()
leftPaddle.goto(-350, 0)


#right paddle
rightPaddle = turtle.Turtle()
rightPaddle.speed(0)
rightPaddle.shape("square")
rightPaddle.color("green")
rightPaddle.shapesize(stretch_wid = 5, stretch_len = 1)
rightPaddle.penup()
rightPaddle.goto(350, 0)


#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("yellow")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = 0.2

#pen to write score
pen = turtle.Turtle()
pen.speed(0)
pen.color("blue")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("score", align = "center", font = ("Arial", 24, "normal"))


#moving left paddle
def leftPaddle_up():
	y = leftPaddle.ycor()
	y = y+90
	leftPaddle.sety(y)


def leftPaddle_down():
	y = leftPaddle.ycor()
	y = y-90
	leftPaddle.sety(y)


#moving right paddle
def rightPaddle_up():
	y = rightPaddle.ycor()
	y = y+90
	rightPaddle.sety(y)


def rightPaddle_down():
	y = rightPaddle.ycor()
	y = y-90
	rightPaddle.sety(y)


#assign keys

window.listen()
window.onkeypress(leftPaddle_up, "w")
window.onkeypress(leftPaddle_down, "s")
window.onkeypress(rightPaddle_up, "Up")
window.onkeypress(rightPaddle_down, "Down")


#ball movement
while True:
	window.update()

	ball.setx(ball.xcor() + ball.dx)
	ball.sety(ball.ycor() + ball.dy)

	#setting border
	if(ball.ycor() > 290):
		ball.sety(290)
		ball.dy = ball.dy*(-1)

	if(ball.ycor() < -290):
		ball.sety(-290)
		ball.dy = ball.dy*(-1)

	if(ball.xcor() > 390):
		ball.goto(0, 0)
		ball.dx = ball.dx*(-1)
		playerA_score += 1
		pen.clear()
		pen.write("Player A: {} Player B: {}".format(playerA_score, playerB_score), align = "center", font = ("Arial", 24, "normal"))

	if(ball.xcor() < -390):
		ball.goto(0, 0)
		ball.dx = ball.dx*(-1)
		playerB_score += 1
		pen.clear()
		pen.write("Player A: {} Player B: {}".format(playerA_score, playerB_score), align = "center", font = ("Arial", 24, "normal"))

	#handling colision
	if((ball.xcor() > 340) and (ball.xcor() < 350) and (ball.ycor() < rightPaddle.ycor() + 40) and (ball.ycor() > rightPaddle.ycor() - 40)):
		ball.setx(340)
		ball.dx = ball.dx*(-1)
	if((ball.xcor() < -340) and (ball.xcor() > -350) and (ball.ycor() < leftPaddle.ycor() + 40) and (ball.ycor() > leftPaddle.ycor() - 40)):
		ball.setx(-340)
		ball.dx = ball.dx*(-1)
	

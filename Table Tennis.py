import turtle
import time

def intro():
    wn = turtle.Screen()
    wn.title("Table Tennis")
    wn.bgcolor("black")
    wn.setup(width=800, height=600)

    intro_text = turtle.Turtle()
    intro_text.color("white")
    intro_text.penup()
    intro_text.hideturtle()
    intro_text.goto(0, 50)
    intro_text.write("Welcome to Table Tennis!", align="center", font=("Courier", 24, "normal"))
    time.sleep(1)
    intro_text.goto(0, -50)
    intro_text.write("Press 'space' to start playing...", align="center", font=("Courier", 18, "normal"))

    wn.listen()

    def start_game():
        intro_text.clear()
        player1_name = wn.textinput("Player 1 Name", "Enter Player 1's name: ")
        player2_name = wn.textinput("Player 2 Name", "Enter Player 2's name: ")
        win_score = int(wn.textinput("What is the win score?", "Enter win score: "))
        game(player1_name, player2_name, win_score)

    wn.onkeypress(start_game, "space")

    wn.mainloop()

def reset_game():
    """
    Function to reset the game and go back to the intro screen
    Instead of closing the turtle window, we call intro again
    """
    turtle.clearscreen()
    intro()

def game(player1_name, player2_name, win_score):
    wn = turtle.Screen()
    wn.title("Table Tennis")
    wn.bgcolor("midnightblue")
    wn.setup(width=800, height=600)
    wn.tracer(0)

    score_a = 0
    score_b = 0

    paddle_a = turtle.Turtle()
    paddle_a.speed(0)
    paddle_a.shape("square")
    paddle_a.color("black")
    paddle_a.shapesize(stretch_len=1, stretch_wid=5)
    paddle_a.penup()
    paddle_a.goto(-350, 0)

    paddle_b = turtle.Turtle()
    paddle_b.speed(0)
    paddle_b.shape("square")
    paddle_b.color("red")
    paddle_b.shapesize(stretch_len=1, stretch_wid=5)
    paddle_b.penup()
    paddle_b.goto(350, 0)

    ball = turtle.Turtle()
    ball.speed(0)
    ball.shape("square")
    ball.color("white")
    ball.penup()
    ball.goto(0, 0)
    ball.dx = 0.25
    ball.dy = -0.25

    pen = turtle.Turtle()
    pen.speed(0)
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)
    pen.write(f"{player1_name}: 0    {player2_name}: 0", align="center", font=("Courier", 24, "normal"))
    pen.goto(0, -260)
    pen.write(f"First to {win_score} wins!", align="center", font=("Courier", 20, "normal"))

    backspace_msg = turtle.Turtle()
    backspace_msg.speed(0)
    backspace_msg.color("white")
    backspace_msg.penup()
    backspace_msg.hideturtle()

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

    wn.listen()
    wn.onkeypress(paddle_a_up, "w")
    wn.onkeypress(paddle_a_down, "s")
    wn.onkeypress(paddle_b_up, "Up")
    wn.onkeypress(paddle_b_down, "Down")

    wn.onkeypress(reset_game, "BackSpace")

    time.sleep(1)

    ball.showturtle()

    time.sleep(1)

    while True:
        wn.update()

        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1

        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1
        
        if ball.xcor() > 390:
            ball.goto(0, 0)
            ball.dx *= -1
            score_a += 1
            pen.clear()
            pen.write(f"{player1_name}: {score_a}    {player2_name}: {score_b}", align="center", font=("Courier", 24, "normal"))
            
            if score_a >= win_score:
                pen.goto(0, 0)
                pen.write(f"{player1_name} WINS!", align="center", font=("Courier", 36, "bold"))
                pen.goto(0, 50)
                pen.write(f"Better Luck Next Time, {player2_name}...", align="center", font=("Courier", 18, "normal"))
                
                backspace_msg.goto(350, -280) 
                backspace_msg.write("Press Backspace to restart", align="right", font=("Courier", 14, "normal"))
                
                break

        if ball.xcor() < -390:
            ball.goto(0, 0)
            ball.dx *= -1
            score_b += 1
            pen.clear()
            pen.write(f"{player1_name}: {score_a}    {player2_name}: {score_b}", align="center", font=("Courier", 24, "normal"))
            
            if score_b >= win_score:
                pen.goto(0, 0)
                pen.write(f"{player2_name} WINS!", align="center", font=("Courier", 36, "bold"))
                pen.goto(0, 50)
                pen.write(f"Better Luck Next Time, {player1_name}...", align="center", font=("Courier", 18, "normal"))
                
                backspace_msg.goto(350, -280) 
                backspace_msg.write("Press Backspace to restart", align="right", font=("Courier", 14, "normal"))
                
                break

        if (ball.xcor() > -350 and ball.xcor() < -340) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
            ball.setx(-340)
            ball.dx *= -1

        if (ball.xcor() < 350 and ball.xcor() > 340) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
            ball.setx(340)
            ball.dx *= -1

intro()

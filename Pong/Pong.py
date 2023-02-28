# Modules
import turtle
import time

class Game:

    def __init__(self, width, height, title, bgcolor):
        self.width = width
        self.height = height
        self.title = title
        self.bgcolor = bgcolor

        self.setup_window()

    def setup_window(self):
        self.window = turtle.Screen()
        self.window.title(self.title)
        self.window.bgcolor(self.bgcolor)
        self.window.setup(width=self.width, height=self.height)
        self.window.tracer(0)

    def update(self):
        self.window.update()

class GameObject:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def init_object(self):
        self.object = turtle.Turtle()
        self.object.speed(0)
        self.object.color("white")
        self.object.penup()
        self.object.goto(self.x, self.y)

class Player(GameObject):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.init_player()

    def init_player(self):
        self.init_object()
        self.object.shape("square")
        self.object.shapesize(stretch_len = 1, stretch_wid = 5)
        self.score = 0

    def up(self):
        if  self.object.ycor() + 50 >= 300:
            self.object.sety(250)
        else:
            y = self.object.ycor() + 20
            self.object.sety(y)

    def down(self):
        if self.object.ycor() - 50 <= -300:
            self.object.sety(-250)
        else:
            y = self.object.ycor() - 20
            self.object.sety(y)

    def input_keys(self, up, down):
        g1.window.listen()
        g1.window.onkeypress(self.up, up)
        g1.window.onkeypress(self.down, down)

class Ball(GameObject):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.init_ball()

    def init_ball(self):
        self.init_object()
        self.object.shape("square")
        self.dx = 3
        self.dy = 3

    def update_pos(self):
        # Move the ball
        
        self.object.setx(self.object.xcor()+self.dx)
        self.object.sety(self.object.ycor()+self.dy)
        if self.object.ycor() + 20 >= 300:
            self.dy *= -1
        if self.object.ycor() - 20 <= -300:
            self.dy *= -1
        if self.object.xcor() > 390:
            self.object.goto(0 , 0)
            self.dx *= -1
            p1.score += 1
            pen.update_score()

        if self.object.xcor() < -390:
            self.object.goto(0 , 0)
            self.dx *= -1
            p2.score += 1
            pen.update_score()

        # Collisions
        if (self.object.xcor() > 330 and self.object.xcor() > -350) and (self.object.ycor() < p2.object.ycor() + 50 and self.object.ycor() > p2.object.ycor() - 50):
            self.object.setx(330)
            self.dx *= -1

        if (self.object.xcor() < -330 and self.object.xcor() > -350) and (self.object.ycor() < p1.object.ycor() + 50 and self.object.ycor() > p1.object.ycor() - 50):
            self.object.setx(-330)
            self.dx *= -1

class Pen(GameObject):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.pen_init()

    def pen_init(self):
        self.init_object()
        self.object.hideturtle()
        self.object.write(f"Player 1 : {p1.score}  Player 2 : {p2.score}",
        align="center", font=("Courier", 24, "normal"))

    def update_score(self):
        self.object.clear()
        self.object.write(f"Player 1 : {p1.score}  Player 2 : {p2.score}",
        align="center", font=("Courier", 24, "normal"))

# Create the game objects
g1 = Game(800, 600, "Pong game", "black")
p1 = Player(-350, 0)
p2 = Player(350, 0)
b1 = Ball(0, 0)
pen = Pen(-20, 260)

# Setup the input keys for the players
p1.input_keys("w", "s")
p2.input_keys("Up", "Down")

# Game loop
while True:
    time.sleep(1 / 500)
    g1.update()
    b1.update_pos()

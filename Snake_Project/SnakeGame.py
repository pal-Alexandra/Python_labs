import time
import turtle


class SnakeGame:
    def __init__(self, width, height, obstacles):
        self.pen = None
        self.head = None
        self.food = None
        self.window = None
        self.width = width
        self.height = height
        self.obstacles = obstacles
        self.init_board()
        self.init_snake()
        self.init_pen()

        self.score = 0
        self.highest_score = 0

        self.delay = 0.1

    def init_board(self):
        self.window = turtle.Screen()
        self.window.title("Snake Game")
        self.window.bgcolor("green")
        self.window.setup(width=self.width, height=self.height)
        self.window.tracer(0)

        for obstacle in self.obstacles:
            x, y = obstacle['x'], obstacle['y']
            obstacle = turtle.Turtle()
            obstacle.speed(0)
            obstacle.shape("square")
            obstacle.color("red")
            obstacle.penup()
            obstacle.goto(x, y)

        self.food = turtle.Turtle()
        self.food.speed(0)
        self.food.shape("circle")
        self.food.color("yellow")
        self.food.penup()
        self.food.goto(0, 100)

    def init_snake(self):
        self.head = turtle.Turtle()
        self.head.speed(0)
        self.head.shape("square")
        self.head.color("black")
        self.head.penup()
        self.head.goto(0, 0)
        self.head.direction = "stop"

    def init_pen(self):
        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.pen.shape("square")
        self.pen.color("white")
        self.pen.penup()
        self.pen.hideturtle()
        x = 0
        y = self.height // 2 - 40
        self.pen.goto(x, y)

    def go_up(self):
        if self.head.direction != "down":
            self.head.direction = "up"

    def go_down(self):
        if self.head.direction != "up":
            self.head.direction = "down"

    def go_left(self):
        if self.head.direction != "right":
            self.head.direction = "left"

    def go_right(self):
        if self.head.direction != "left":
            self.head.direction = "right"

    def configure_key_bindings(self):
        self.window.onkeypress(self.go_up, "w")
        self.window.onkeypress(self.go_down, "s")
        self.window.onkeypress(self.go_left, "a")
        self.window.onkeypress(self.go_right, "d")

    def move(self):
        if self.head.direction == "up":
            y = self.head.ycor()
            self.head.sety(y + 20)

        if self.head.direction == "down":
            y = self.head.ycor()
            self.head.sety(y - 20)

        if self.head.direction == "left":
            x = self.head.xcor()
            self.head.setx(x - 20)

        if self.head.direction == "right":
            x = self.head.xcor()
            self.head.setx(x + 20)

    def start_game(self):
        self.window.listen()
        self.configure_key_bindings()

        while True:
            self.window.update()
            self.move()
            time.sleep(self.delay)

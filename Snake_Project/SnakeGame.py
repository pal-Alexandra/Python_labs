import turtle


class SnakeGame:
    def __init__(self, width, height, obstacles):
        self.width = width
        self.height = height
        self.obstacles = obstacles
        self.init_board()
        self.init_snake()
        self.init_pen()

    def init_board(self):
        window = turtle.Screen()
        window.title("Snake Game")
        window.bgcolor("green")
        window.setup(width=self.width, height=self.height)
        window.tracer(0)

        for obstacle in self.obstacles:
            x, y = obstacle['x'], obstacle['y']
            obstacle = turtle.Turtle()
            obstacle.speed(0)
            obstacle.shape("square")
            obstacle.color("red")
            obstacle.penup()
            obstacle.goto(x, y)

        food = turtle.Turtle()
        food.speed(0)
        food.shape("circle")
        food.color("yellow")
        food.penup()
        food.goto(0, 100)

    def init_snake(self):
        head = turtle.Turtle()
        head.speed(0)
        head.shape("square")
        head.color("black")
        head.penup()
        head.goto(0, 0)
        head.direction = "stop"

    def init_pen(self):
        pen = turtle.Turtle()
        pen.speed(0)
        pen.shape("square")
        pen.color("white")
        pen.penup()
        pen.hideturtle()

        x = 0
        y = self.height // 2 - 40
        pen.goto(x, y)

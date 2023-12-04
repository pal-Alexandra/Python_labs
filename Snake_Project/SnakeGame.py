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
    
    def start_game(self):
        self.window.listen()
        self.window.update()

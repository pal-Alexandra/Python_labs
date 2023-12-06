import time
import turtle
import random
from PIL import Image


class SnakeGame:
    def __init__(self, width, height, obstacles):
        self.pen = None
        self.head = None
        self.segments = []
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

        self.game_is_over = False

        self.delay = 0.1

    def init_board(self):
        self.window = turtle.Screen()
        self.window.title("Snake Game")
        self.window.setup(width=self.width, height=self.height)

        original_image = Image.open("background.gif")
        resized_image = original_image.resize((self.width, self.height))
        resized_image.save("resized_background.gif")
        self.window.bgpic("resized_background.gif")

        self.window.tracer(0)

        for obstacle in self.obstacles:
            x, y = obstacle['x'], obstacle['y']
            obstacle = turtle.Turtle()
            obstacle.speed(0)
            # obstacle.shape("square")
            # obstacle.color("red")
            self.window.register_shape("wall.gif")
            obstacle.shape("wall.gif")
            obstacle.penup()
            obstacle.goto(x, y)

    def init_food(self):
        self.food = turtle.Turtle()
        self.food.speed(0)
        # self.food.shape("circle")
        # self.food.color("yellow")
        self.window.register_shape("food.gif")
        self.food.shape("food.gif")
        self.food.penup()
        self.food.goto(0, 100)

    def init_snake(self):
        self.head = turtle.Turtle()
        self.head.speed(0)
        self.head.shape("square")
        self.head.color("dark green")
        self.head.shapesize(1.3, 1.3)
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

    def is_collision(self, x, y):
        if self.head.distance(x, y) < 20:
            return True
        return False

    def is_collision_with_border(self):
        if self.head.xcor() > self.width / 2 - 20 or self.head.xcor() < -self.width / 2 + 20 or self.head.ycor() > self.height / 2 - 20 or self.head.ycor() < -self.height / 2 + 20:
            return True
        return False

    def end_game(self):
        self.pen.clear()
        self.pen.color("blue")
        self.pen.write(f"GAME OVER! Your score: {self.score} Highest Score: {self.highest_score}", align="center",
                       font=("Courier", 20, "underline", "bold"))

        self.pen.goto(0, -50)
        self.pen.write(f"Press 'C' play again or 'E' to exit game", align="center",
                       font=("Courier", 24, "underline", "bold"))

        self.pen.color("white")

        self.window.listen()

        def restart_game():
            time.sleep(1)
            self.head.goto(0, 0)
            self.head.direction = "stop"

            # hide the segments
            for segment in self.segments:
                segment.goto(1000, 1000)
            self.segments.clear()

            self.food.goto(1000, 1000)

            # reset score
            self.score = 0

            # reset delay
            self.delay = 0.1

            # reset pen position
            x = 0
            y = self.height // 2 - 40
            self.pen.goto(x, y)
            self.pen.clear()
            self.pen.write(f"Score: {self.score}  Highest Score: {self.highest_score}", align="center",
                           font=("Courier", 24, "normal"))

            self.start_game()

        def exit_game():
            # self.window.bye()
            # exit(0)
            self.game_is_over = True
            self.pen.clear()
            self.pen.goto(0, 0)
            self.pen.color("blue")
            self.pen.write(f"Highest Score: {self.highest_score}", align="center",
                           font=("Courier", 24, "underline", "bold"))

        self.window.onkey(restart_game, "c")
        self.window.onkey(exit_game, "e")
        self.window.mainloop()

    def start_game(self):
        self.init_food()
        self.window.listen()
        self.configure_key_bindings()

        self.game_is_over = False

        while not self.game_is_over:
            self.window.update()

            # collision with border
            if self.is_collision_with_border():
                time.sleep(1)
                self.game_is_over = True
                self.end_game()

            # collision with obstacles
            for obstacle in self.obstacles:
                if self.is_collision(obstacle["x"], obstacle["y"]):
                    time.sleep(1)
                    self.game_is_over = True
                    self.end_game()

            # collision with food
            if self.is_collision(self.food.xcor(), self.food.ycor()):
                # move food to random location
                x_food = random.randint(-self.width / 2 + 20, self.width / 2 - 20)
                y_food = random.randint(-self.height / 2 + 20, self.height / 2 - 20)
                self.food.goto(x_food, y_food)

                # snake go bigger => add a new segment to the snake
                new_segment = turtle.Turtle()
                new_segment.speed(0)
                new_segment.shape("square")
                new_segment.color("lime green")
                new_segment.shapesize(1.3, 1.3)
                new_segment.penup()
                self.segments.append(new_segment)

                self.delay -= 0.001

                # increase score
                self.score += 10
                if self.score > self.highest_score:
                    self.highest_score = self.score
                self.pen.clear()
                self.pen.write(f"Score: {self.score}  Highest Score: {self.highest_score}", align="center",
                               font=("Courier", 24, "normal"))

            # move snake's segments
            for index in range(len(self.segments) - 1, 0, -1):
                x = self.segments[index - 1].xcor()
                y = self.segments[index - 1].ycor()
                self.segments[index].goto(x, y)
            if len(self.segments) > 0:
                x = self.head.xcor()
                y = self.head.ycor()
                self.segments[0].goto(x, y)

            self.move()

            # collision with snake's body
            for segment in self.segments:
                if self.is_collision(segment.xcor(), segment.ycor()):
                    time.sleep(1)
                    self.end_game()

            time.sleep(self.delay)

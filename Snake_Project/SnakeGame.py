import time
import turtle
import random
from PIL import Image


class SnakeGame:
    def __init__(self, width, height, obstacles):
        self.pen = None
        self.head = None
        self.tail = None
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
        """
        Initialize the board and set images for background and obstacles. It sets the:
            width of the board
            height of the board
            obstacles

        :return: None
        """
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
        """
        Initialize the food for the snake. It sets the coordinates of the food at the beginning of the game and sets
        the image for food.
        :return: None
        """
        self.food = turtle.Turtle()
        self.food.speed(0)
        # self.food.shape("circle")
        # self.food.color("yellow")
        self.window.register_shape("food.gif")
        self.food.shape("food.gif")
        self.food.penup()
        self.food.goto(0, 100)

    def init_snake(self):
        """
        Initialize the snake. It sets the coordinates of the snake at the beginning of the game.
        :return: None
        """
        self.head = turtle.Turtle()
        self.head.speed(0)
        self.head.shape("square")
        self.head.color("dark green")
        self.head.shapesize(1.3, 1.3)
        self.head.penup()
        self.head.goto(0, 0)
        self.head.direction = "stop"

        self.tail = turtle.Turtle()
        self.tail.speed(0)
        self.tail.shape("square")
        self.tail.color("yellow")
        self.tail.shapesize(1.3, 1.3)
        self.tail.penup()
        self.tail.goto(0, -20)


    def init_pen(self):
        """
        Initialize the pen. It sets the coordinates of the pen at the beginning of the game.
        :return: None
        """
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
        """
        Change the direction of the snake to up.
        :return: None
        """
        if self.head.direction != "down":
            self.head.direction = "up"

    def go_down(self):
        """
        Change the direction of the snake to down.
        :return: None
        """
        if self.head.direction != "up":
            self.head.direction = "down"

    def go_left(self):
        """
        Change the direction of the snake to left.
        :return: None
        """
        if self.head.direction != "right":
            self.head.direction = "left"

    def go_right(self):
        """
        Change the direction of the snake to right.
        :return: None
        """
        if self.head.direction != "left":
            self.head.direction = "right"

    def configure_key_bindings(self):
        """
        Configure the key controls for the game.
        :return: None
        """
        self.window.onkeypress(self.go_up, "w")
        self.window.onkeypress(self.go_down, "s")
        self.window.onkeypress(self.go_left, "a")
        self.window.onkeypress(self.go_right, "d")

    def move(self):
        """
        Move the snake in the direction of the head.
        :return: None
        """
        if self.head.direction == "up":
            y = self.head.ycor()
            self.head.sety(y + 20)

            if len(self.segments) == 0:
                self.tail.goto(self.head.xcor(), self.head.ycor() - 18)

        elif self.head.direction == "down":
            y = self.head.ycor()
            self.head.sety(y - 20)

            if len(self.segments) == 0:
                # Set the initial position of the tail to be the first segment
                self.tail.goto(self.head.xcor(), self.head.ycor() + 18)

        elif self.head.direction == "left":
            x = self.head.xcor()
            self.head.setx(x - 20)

            if len(self.segments) == 0:
                self.tail.goto(self.head.xcor() + 18, self.head.ycor())

        elif self.head.direction == "right":
            x = self.head.xcor()
            self.head.setx(x + 20)

            if len(self.segments) == 0:
                self.tail.goto(self.head.xcor() - 18, self.head.ycor())

    def is_collision_with_obstacle(self, x, y):
        """
        Check if the snake's head is colliding with an obstacle.
        :param x: coordinate x of the obstacle
        :param y: coordinate y of the obstacle
        :return: None
        """
        if self.head.distance(x, y) < 25:
            return True
        return False

    def is_collision(self, x, y):
        if self.head.distance(x, y) < 20:
            return True
        return False

    def is_collision_with_border(self):
        """
        Check if the snake's head is colliding with the border.
        :return: None
        """
        if self.head.xcor() > self.width / 2 - 20 or self.head.xcor() < -self.width / 2 + 20 or self.head.ycor() > self.height / 2 - 20 or self.head.ycor() < -self.height / 2 + 20:
            return True
        return False

    def end_game(self):
        """
        Logic for ending the game: show the score, highest score and ask the user if he wants to play again or exit the game.
        :return: None
        """
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
            """
            Logic for restarting the game. Reset the snake's head, segments, food, score, delay and pen position.
            :return:
            """
            time.sleep(1)
            self.head.goto(0, 0)
            self.tail.goto(0, -20)
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
            """
            Logic for exiting the game: showing the highest score and ening the game.
            :return:
            """
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
        """
        Logic for starting the game: initialize the food, listen for key bindings, configure the key bindings,
        check for collisions with border, obstacles, food, snake's body, move the snake's segments.
        :return: None
        """
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
                if self.is_collision_with_obstacle(obstacle["x"], obstacle["y"]):
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
            if len(self.segments) > 0:
                self.tail.goto(self.segments[-1].xcor(), self.segments[-1].ycor())

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
            for index in range(1, len(self.segments)):
                if self.is_collision(self.segments[index].xcor(), self.segments[index].ycor()):
                    time.sleep(1)
                    self.end_game()
            if self.head.distance(self.tail.xcor(), self.tail.ycor()) < 20 and len(self.segments) > 0:
                time.sleep(1)
                self.end_game()

            time.sleep(self.delay)

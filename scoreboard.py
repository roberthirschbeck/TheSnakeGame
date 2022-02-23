from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.counter = 0
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=280)
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Counter: {self.counter}", move=False, align="center", font='Calibri')

    def update_counter(self):
        self.counter += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(x=0, y=0)
        self.write("Game over", move=False, align="center", font='Calibri')

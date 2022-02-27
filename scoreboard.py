from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.counter = 0
        # self.high_score = 0
        with open("highscore.txt", mode="r") as f:
            self.high_score = int(f.read())
            print(self.high_score)
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=280)
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Counter: {self.counter} High Score: {self.high_score}", move=False, align="center", font='Calibri')

    def update_counter(self):
        self.counter += 1
        self.clear()
        self.update_scoreboard()

    # def read_high_score(self):
    #     with open("highscore.txt", mode="r") as f:
    #         self.high_score = f.read()
    #         print(self.high_score)

    def write_high_score(self):
        with open("highscore.txt", mode="w") as f:
            f.write(f"{self.high_score}")

    def reset(self):
        if self.counter > self.high_score:
            self.high_score = self.counter
            self.write_high_score()
        self.counter = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(x=0, y=0)
    #     self.write("Game over", move=False, align="center", font='Calibri')

from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.update_scoreboard()
        self.hideturtle()
    
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", False, "center",("Courier", 24, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",False, "center",("Courier", 24, "normal"))
        

    def increase_score(self):
        self.clear()
        self.score +=1
        self.update_scoreboard()



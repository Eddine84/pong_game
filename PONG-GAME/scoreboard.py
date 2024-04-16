from  turtle import Turtle
ALIGNEMENT = "center"
FONT = ("Courier",24,"normal")
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.update_score()
        
    def update_score(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.l_score, align=ALIGNEMENT ,font=FONT)
        self.goto(100,200)
        self.write(self.r_score, align=ALIGNEMENT ,font=FONT)

    def update_l_score(self):
        self.l_score+=1
        self.update_score()
    def update_r_score(self):
        self.r_score+=1
        self.update_score()
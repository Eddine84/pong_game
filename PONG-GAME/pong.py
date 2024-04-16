from turtle import Turtle



class Pong(Turtle):
    def __init__(self,position):
        super().__init__()
        self.create_paddle(position)

    def create_paddle(self,position):
        self.penup()
        self.goto(position)
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        

    def go_up(self):
        new_y_position = self.ycor() + 20
        self.goto(self.xcor() ,new_y_position)
        
        
    def go_down(self):
       new_y_position = self.ycor() -  20
       self.goto(self.xcor() ,new_y_position)
           
        

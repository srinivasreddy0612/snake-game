from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segment = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segmengt = Turtle("square")
            new_segmengt.color("white")
            new_segmengt.penup()
            new_segmengt.goto(position)
            self.segment.append(new_segmengt)

    def move(self):
        for seg_num in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[seg_num - 1].xcor()
            new_y = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(new_x, new_y)
        self.segment[0].fd(MOVE_DISTANCE)

    def enlarge(self):
        xc = self.segment[-1].xcor()
        yc = self.segment[-1].ycor()
        new_segmengt = Turtle("square")
        new_segmengt.color("white")
        new_segmengt.penup()
        new_segmengt.goto(xc, yc)
        self.segment.append(new_segmengt)

    def restart(self):
        for x in self.segment:
            x.goto(1000, 1000)
        self.segment.clear()
        self.create_snake()

    def up(self):
        if self.segment[0].heading() != DOWN:
            self.segment[0].setheading(UP)

    def left(self):
        if self.segment[0].heading() != RIGHT:
            self.segment[0].setheading(LEFT)

    def down(self):
        if self.segment[0].heading() != UP:
            self.segment[0].setheading(DOWN)

    def right(self):
        if self.segment[0].heading() != LEFT:
            self.segment[0].setheading(RIGHT)

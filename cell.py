from graphics import Line, Point, Window

class Cell:
    def __init__(self, top_left:Point, bottom_right:Point, window:Window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.top_left = top_left
        self.bottom_right = bottom_right
        self.top_right = Point(self.bottom_right.x, self.top_left.y)
        self.bottom_left = Point(self.top_left.x, self.bottom_right.y)
        self.center = Point((self.top_left.x + self.bottom_right.x)/2, (self.top_left.y + self.bottom_right.y)/2)
        self.window = window

    def draw(self):
        if self.has_top_wall:
            Line(self.top_left, self.top_right).draw(self.window.canvas)
        if self.has_bottom_wall:
            Line(self.bottom_left, self.bottom_right).draw(self.window.canvas)
        if self.has_left_wall:
            Line(self.top_left, self.bottom_left).draw(self.window.canvas)
        if self.has_right_wall:
            Line(self.top_right, self.bottom_right).draw(self.window.canvas)

    def draw_move(self, other, undo=False):
        connect_line = Line(self.center, other.center)
        if undo:
            connect_line.draw(self.window.canvas, "gray")
        else:
            connect_line.draw(self.window.canvas, "red")
from tkinter import Tk, BOTH, Canvas

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, p1:Point, p2:Point):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas:Canvas, fill_color:str):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2)
        canvas.pack()


class Window:
    def __init__(self, width:int, height:int):
        self.root_widget = Tk()
        self.root_widget.title("MazeSolver")
        self.canvas = Canvas(self.root_widget, bg="white", height=height, width=width)
        self.canvas.pack()
        self.is_running = False
        self.root_widget.protocol("WM_DELETE_WINDOW", self.close)


    def redraw(self):
        self.root_widget.update_idletasks()
        self.root_widget.update()

    
    def wait_for_close(self):
        self.is_running = True
        while self.is_running:
            self.redraw()

    def close(self):
        self.is_running = False

    def draw_line(self, line:Line, fill_color="black"):
        line.draw(self.canvas, fill_color)



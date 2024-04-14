from graphics import Window, Line, Point
from cell import Cell
from maze import Maze

def main():
    win = Window(800, 600)
    p1 = Point(100, 100)
    p2 = Point(200, 200)
 
    

    #cell1 = Cell(p1, p2, win)
    #cell2 = Cell(Point(300, 300), Point(400, 400), win)
    #cell1.draw()
    #cell2.draw()
    #cell1.draw_move(cell2)

    maze = Maze(1, 1, 3, 3, 100, 100, win)

    win.wait_for_close()




if __name__ == "__main__":
    main()

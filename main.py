from graphics import Window, Line, Point, Cell

def main():
    win = Window(800, 600)
    p1 = Point(100, 100)
    p2 = Point(200, 200)
 
    

    cell1 = Cell(p1, p2, win)
    cell1.draw()

    win.wait_for_close()




if __name__ == "__main__":
    main()

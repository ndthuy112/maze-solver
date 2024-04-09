from graphics import Window, Line, Point

def main():
    win = Window(800, 600)
    p1 = Point(0, 0)
    p2 = Point(200, 200)
    line1 = Line(p1, p2)
    win.draw_line(line1, "red")
    win.wait_for_close()




if __name__ == "__main__":
    main()

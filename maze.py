from time import sleep
from cell import Cell, Point
from graphics import Window


class Maze:
    def __init__(self, x1, y1, num_rows: int, num_cols: int, cell_size_x, cell_size_y, win:Window):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = []
        self._create_cells()


    def _create_cells(self):
        current_x = self.x1
        current_y = self.y1
        for i in range(self.num_rows):
            row = []
            for j in range(self.num_cols):
                top_left = Point(current_x, current_y)
                bottom_right = Point((current_x + self.cell_size_x), (current_y + self.cell_size_y))
                row.append(Cell(top_left, bottom_right, self.win))
                current_x += self.cell_size_x
            self._cells.append(row)
            current_x = self.x1
            current_y += self.cell_size_y

        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self._draw_cells(i, j)

        #draw_cell


    def _draw_cells(self, i, j):
        self._cells[i][j].draw()
        self._animate()


    def _animate(self):
        self.win.redraw()
        sleep(0.1)
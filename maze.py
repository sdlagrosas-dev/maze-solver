
from cell import Cell
from time import sleep

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win,
    ) -> None:
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win

        self._create_cells()


    def _create_cells(self):
        self.cells = []
        for i in range(self.num_rows):
            self.cells.append([])
            for j in range(self.num_cols):
                new_cell = self._draw_cell(i, j)
                self.cells[i].append(new_cell)


    def _draw_cell(self, i, j):
        new_cell = Cell(self.x1 + j * self.cell_size_x,
            self.y1 + i * self.cell_size_y,
            self.x1 + (j + 1) * self.cell_size_x,
            self.y1 + (i + 1) * self.cell_size_y,
            self.win,
            )
        new_cell.draw()
        self._animate()
        
        return new_cell

    def _animate(self):
        self.win.redraw()
        sleep(0.05)
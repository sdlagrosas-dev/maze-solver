from cell import Cell
from time import sleep
import random


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
        seed=None,
    ) -> None:
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win

        if seed is not None:
            random.seed(seed)

        self._create_cells()

    def _create_cells(self):
        """
        Populate self._cells with Cell objects.
        self._cells is a 2D list, where self._cells[i][j] is the Cell at row i and column j.
        Each Cell is drawn to the Window.
        After each Cell is drawn, the Window is redrawn with a short delay to animate the creation of the maze.
        """

        self._cells = []
        for i in range(self.num_rows):
            self._cells.append([])
            for j in range(self.num_cols):
                new_cell = self._draw_cell(i, j)
                self._cells[i].append(new_cell)

    def _draw_cell(self, i, j):
        """
        Create a Cell at row i and column j and draw it to the Window.
        The cell is drawn by calling its draw method.
        After drawing, the Window is redrawn with a short delay to animate the creation of the maze.
        Returns the newly created Cell.
        """
        new_cell = Cell(
            self.x1 + j * self.cell_size_x,
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

    def break_entrance_and_exit(self):
        entrance = self._cells[0][0]
        exit = self._cells[self.num_rows - 1][self.num_cols - 1]

        entrance._has_top_wall = False
        exit._has_bottom_wall = False

        entrance.draw()
        exit.draw()

        self._animate()

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True

        while True:
            unvisited = []
            
            if i > 0 and not self._cells[i - 1][j].visited:
                unvisited.append((i - 1, j))
            if j > 0 and not self._cells[i][j - 1].visited:
                unvisited.append((i, j - 1))
            if i < self.num_rows - 1 and not self._cells[i + 1][j].visited:
                unvisited.append((i + 1, j))
            if j < self.num_cols - 1 and not self._cells[i][j + 1].visited:
                unvisited.append((i, j + 1))

            if len(unvisited) == 0:
                break

            next_i, next_j = random.choice(unvisited)

            if i > next_i:
                self._cells[i][j]._has_top_wall = False
                self._cells[next_i][next_j]._has_bottom_wall = False
            if i < next_i:
                self._cells[i][j]._has_bottom_wall = False
                self._cells[next_i][next_j]._has_top_wall = False
            if j > next_j:
                self._cells[i][j]._has_left_wall = False
                self._cells[next_i][next_j]._has_right_wall = False
            if j < next_j:
                self._cells[i][j]._has_right_wall = False
                self._cells[next_i][next_j]._has_left_wall = False

            self._cells[i][j].draw()
            self._cells[next_i][next_j].draw()
            self._animate()
            
            self._break_walls_r(next_i, next_j)

    def _reset_cells_visited(self):
        for r in range(self.num_rows):
            for c in range(self.num_cols):
                self._cells[r][c].visited = False

    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j) -> bool: 
        self._animate()
        print(f"Cell: {i},{j}")
        self._cells[i][j].visited = True

        if i == self.num_rows-1 and j == self.num_cols-1:
            return True
        
        if i < self.num_rows - 1 and not self._cells[i + 1][j].visited and not self._cells[i][j]._has_bottom_wall:
            self._cells[i][j].draw_move(self._cells[i + 1][j])
            move_down_result = self._solve_r(i + 1, j)
            if move_down_result:
                return move_down_result
            else:
                self._cells[i][j].draw_move(self._cells[i + 1][j], undo=True)
        if j < self.num_cols - 1 and not self._cells[i][j + 1].visited and not self._cells[i][j]._has_right_wall:
            self._cells[i][j].draw_move(self._cells[i][j + 1])
            move_right_result = self._solve_r(i, j + 1)
            if move_right_result:
                return move_right_result
            else:
                self._cells[i][j].draw_move(self._cells[i][j + 1], undo=True)
        if i > 0 and not self._cells[i - 1][j].visited and not self._cells[i][j]._has_top_wall:
            self._cells[i][j].draw_move(self._cells[i - 1][j])
            move_up_result = self._solve_r(i - 1, j)
            if move_up_result:
                return move_up_result
            else:
                self._cells[i][j].draw_move(self._cells[i - 1][j], undo=True)
        if j > 0 and not self._cells[i][j - 1].visited and not self._cells[i][j]._has_left_wall:
            self._cells[i][j].draw_move(self._cells[i][j - 1])
            move_left_result = self._solve_r(i, j - 1)
            if move_left_result:
                return move_left_result
            else:
                self._cells[i][j].draw_move(self._cells[i][j - 1], undo=True)
        
        return False





import unittest

from maze import Maze
from window import Window

class Tests(unittest.TestCase):
    # def test_maze_create_cells(self):
    #     win = Window(800, 600)
    #     num_cols = 12
    #     num_rows = 10
    #     m1 = Maze(0, 0, num_rows, num_cols, 20, 20, win)
    #     self.assertEqual(
    #         len(m1._cells),
    #         num_rows,
    #     )
    #     self.assertEqual(
    #         len(m1._cells[0]),
    #         num_cols,
    #     )

    # def test_maze_break_entrance_and_exit(self):
    #     win = Window(800, 600)
    #     num_cols = 12
    #     num_rows = 10
    #     m1 = Maze(100, 100, num_rows, num_cols, 20, 20, win)
    #     m1.break_entrance_and_exit()

    def test_maze_break_walls_r(self):
        win = Window(800, 600)
        num_cols = 5
        num_rows = 5
        m1 = Maze(100, 100, num_rows, num_cols, 30, 30, win)
        m1.break_entrance_and_exit()
        m1._break_walls_r(num_cols//2, num_rows//2)
        m1._reset_cells_visited()

    def test_maze_solve_r(self):
        win = Window(800, 600)
        num_cols = 10
        num_rows = 10
        m1 = Maze(100, 100, num_rows, num_cols, 40, 40, win)
        m1.break_entrance_and_exit()
        m1._break_walls_r(0, 0)
        m1._reset_cells_visited()
        m1.solve()



if __name__ == "__main__":
    unittest.main()
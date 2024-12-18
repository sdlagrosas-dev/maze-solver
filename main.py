from window import Window
from point import Point
from line import Line
from cell import Cell
from maze import Maze


def main():
    win = Window(800, 600)

    # Test maze solve
    num_cols = 12
    num_rows = 10
    m1 = Maze(50, 50, num_rows, num_cols, 50, 50, win)
    m1.break_entrance_and_exit()
    m1._break_walls_r(num_cols//2, num_cols//2)
    m1._reset_cells_visited()

    result = m1.solve()
    print(result)

    # Close window
    win.wait_for_close()


if __name__ == "__main__":
    main()

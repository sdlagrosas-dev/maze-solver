from window import Window
from point import Point
from line import Line
from cell import Cell
from maze import Maze


def main():
    win = Window(800, 600)

    # Test draw_line
    # line_1 = Line(Point(0, 0), Point(100, 100))
    # line_2 = Line(Point(0, 100), Point(100, 0))
    # win.draw_line(line_1, "red")
    # win.draw_line(line_2, "black")

    # Test draw cells
    # cell_1 = Cell(1, 1, 100, 100, win)
    # cell_1.draw()

    # cell_2 = Cell(100, 1, 200, 100, win)
    # cell_2.draw()

    # cell_3 = Cell(200, 1, 300, 100, win)
    # cell_3.draw()

    # cell_4 = Cell(300, 1, 400, 100, win)
    # cell_4.draw()

    # # Test draw move
    # cell_1.draw_move(cell_2, True)
    # cell_2.draw_move(cell_3)
    # cell_3.draw_move(cell_4, True)

    # Test maze
    maze = Maze(1, 1, 6, 8, 100, 100, win)

    # Close window
    win.wait_for_close()


if __name__ == "__main__":
    main()

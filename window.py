from tkinter import Tk, BOTH, Canvas
from line import Line


class Window:
    def __init__(self, width, height) -> None:
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.geometry(f"{width}x{height}")
        self.canvas = Canvas(self.__root, bg="white", width=width, height=height)
        self.canvas.pack()
        self.is_running = False

        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def draw_line(self, line: Line, fill_color, width=1):
        line.draw(self.canvas, fill_color, width)

    def wait_for_close(self):
        self.is_running = True
        while self.is_running:
            self.redraw()

    def close(self):
        self.is_running = False

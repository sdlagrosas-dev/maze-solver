from window import Window
from point import Point
from line import Line


class Cell:
    def __init__(
        self,
        _x1,
        _y1,
        _x2,
        _y2,
        _win: Window,
        has_left_wall=True,
        has_right_wall=True,
        has_top_wall=True,
        has_bottom_wall=True,
    ) -> None:
        self._x1 = _x1
        self._y1 = _y1
        self._x2 = _x2
        self._y2 = _y2
        self._win = _win
        self._has_left_wall = has_left_wall
        self._has_right_wall = has_right_wall
        self._has_top_wall = has_top_wall
        self._has_bottom_wall = has_bottom_wall

    def draw(self):
        if self._has_left_wall:
            self._win.draw_line(
                Line(Point(self._x1, self._y1), Point(self._x1, self._y2)),
                "black",
            )

        if self._has_right_wall:
            self._win.draw_line(
                Line(Point(self._x2, self._y1), Point(self._x2, self._y2)),
                "black",
            )

        if self._has_top_wall:
            self._win.draw_line(
                Line(Point(self._x1, self._y1), Point(self._x2, self._y1)),
                "black",
            )

        if self._has_bottom_wall:
            self._win.draw_line(
                Line(Point(self._x1, self._y2), Point(self._x2, self._y2)),
                "black",
            )

    def draw_move(self, to_cell, undo=False):
        center_point = Point((self._x1 + self._x2) // 2, (self._y1 + self._y2) // 2)
        to_center_point = Point(
            (to_cell._x1 + to_cell._x2) // 2, (to_cell._y1 + to_cell._y2) // 2
        )
        if not undo:
            self._win.draw_line(
                Line(center_point, to_center_point),
                "red",
            )

        else:
            self._win.draw_line(
                Line(center_point, to_center_point),
                "gray",
            )

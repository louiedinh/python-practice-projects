import curses

from datastructures import Point


class Screen:

    CELL_CHAR = ord("o")
    BLANK_CHAR= ord(" ")

    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.max_row, self.max_col = self.stdscr.getmaxyx()
        self.max_row -= 1
        self.max_col -= 1
        self.origin = Point(0,0)
        self.saved_cursors = []

    # Declare cursor_position as a property
    @property
    def cursor_position(self) -> Point:
        """
        Returns the absolute cursor position
        """
        relative_row, relative_col = self.stdscr.getyx()
        return self.__get_absolute_point(Point(relative_row, relative_col))

    def get_input_key(self):
        return self.stdscr.getkey()

    def move_origin(self, row_delta, col_delta):
        """ 
        Move the origin
        """
        self.origin = Point(self.origin.row + row_delta, self.origin.col + col_delta)

    def move_cursor(self, row_delta, col_delta):
        """ 
        Move the cursor
        """
        row, col = self.stdscr.getyx()
        try:
            self.stdscr.move(row + row_delta, col + col_delta)
        except curses.error:
           # Tried to move off the screen
            return False

        return True

    def add_cell(self, point):
        # Transform point to be relative to origin
        relative_point = self.__get_relative_point(absolute_point=point)
        # Insert the actual character
        if relative_point.row > self.max_row or relative_point.col > self.max_col or relative_point.row < 0 or relative_point.col < 0:
            return
        self.save_cursor()
        self.stdscr.move(relative_point.row, relative_point.col)
        self.stdscr.addch(self.CELL_CHAR)
        self.restore_cursor()

    def remove_cell(self, point):
        relative_point = self.__get_relative_point(absolute_point=point)
        self.save_cursor()
        self.stdscr.move(relative_point.row, relative_point.col)
        self.stdscr.addch(self.BLANK_CHAR)
        self.restore_cursor()

    def save_cursor(self):
        row, col = self.stdscr.getyx()
        self.saved_cursors.append(Point(row, col))

    def restore_cursor(self):
        saved_cursor = self.saved_cursors.pop()
        self.stdscr.move(saved_cursor.row, saved_cursor.col)

    def clear(self):
        self.stdscr.erase()

    def __get_relative_point(self, absolute_point):
        return Point(absolute_point.row - self.origin.row, absolute_point.col - self.origin.col)

    def __get_absolute_point(self, relative_point):
        return Point(relative_point.row + self.origin.row, relative_point.col + self.origin.col)



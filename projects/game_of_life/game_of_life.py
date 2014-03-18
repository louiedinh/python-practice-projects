"""
TODOS:
    - Add a status bar the bottom to show mode
    - Add a draw screen function to print out statistics
    - Think of a better way to save/restore cursor
"""

import curses

from board import Board
from screen import Screen
from datastructures import Point, Vector


class Command:
    """
    Stores the valid user input commands
    """
    MOVE_KEYS = ['KEY_LEFT', 'KEY_RIGHT', 'KEY_UP', 'KEY_DOWN']

    INSERT_MODE = 'i'
    NORMAL_MODE = 'n'
    PAN_MODE = 'p'
    RECORD_MODE = 'r'
    REPLAY_MODE = 'e'

    INSERT_CELL= 'c'
    DELETE_CELL = 'x'
    QUIT = 'q'
    STEP = ' '
    SAVE_BOARD = 's'
    LOAD_BOARD = 'l'
    
    @staticmethod
    def cursor_transform_for_command(key):
        """
        Returns a Vector representing how the cursor should be transformed 
        """
        if key == 'KEY_LEFT':
            return Vector(row=0, col=-1)
        elif key == 'KEY_RIGHT':
            return Vector(row=0, col=1)
        elif key == 'KEY_UP':
            return Vector(row=-1, col=0)
        elif key == 'KEY_DOWN':
            return Vector(row=1, col=0)
        else:
            raise ValueError("{} does not map to a transformation".format(key))

class Mode:
    INSERT = 1
    NORMAL = 2
    PAN = 3
    RECORD = 4
    REPLAY = 5

    def get_code(self):
        pass

class InsertMode(Mode):
    def get_code(self):
        return 1

    def dispatch_user_command(self, gol, input_key):
        if input_key in Command.MOVE_KEYS:
            transform = Command.cursor_transform_for_command(input_key)
            gol.add_cell(gol.screen.cursor_position)
            gol.screen.move_cursor(row_delta=transform.row, col_delta=transform.col)

class NormalMode(Mode):
    def get_code(self):
        return 2

    def dispatch_user_command(self, gol, input_key):
        if input_key in Command.MOVE_KEYS:
            transform = Command.cursor_transform_for_command(input_key)
            gol.screen.move_cursor(row_delta=transform.row, col_delta=transform.col)
        elif input_key == Command.STEP:
            gol.step()

class PanMode(Mode):
    def get_code(self):
        return 3

    def dispatch_user_command(self, gol, input_key):
        if input_key in Command.MOVE_KEYS:
            transform = Command.cursor_transform_for_command(input_key)
            gol.screen.move_origin(transform.row, transform.col)
            gol.refresh_screen()

class RecordMode(Mode):
    def get_code(self):
        return 4

    def dispatch_user_command(self, gol, input_key):
        if input_key == Command.STEP:
            gol.record()
            gol.step()
        elif input_key in Command.MOVE_KEYS:
            transform = Command.cursor_transform_for_command(input_key)
            gol.screen.move_cursor(row_delta=transform.row, col_delta=transform.col)

class ReplayMode(Mode):
    def get_code(self):
        return 5

    def dispatch_user_command(self, gol, input_key):
        if input_key == Command.STEP:
            gol.replay_step()

class GameOfLife:
    """
    An instance of the game of life.
    """
    SAVE_FILENAME = "saved_game.gol"
    RECORD_FILENAME = "recorded_game.gol"
    REPLAY_FILENAME = "replay_game.gol"

    def __init__(self, stdscr):
        self.mode = Mode.NORMAL
        self.screen = Screen(stdscr)
        self.board = Board()
        self.start()

    @property
    def mode(self):
        return self._mode.get_code()
    @mode.setter
    def mode(self, value):
        if value == Mode.INSERT:
            self._mode = InsertMode()
        elif value == Mode.NORMAL:
            self._mode = NormalMode()
        elif value == Mode.PAN:
            self._mode = PanMode()
        elif value == Mode.RECORD:
            self._mode = RecordMode()
        elif value == Mode.REPLAY:
            self._mode = ReplayMode()

    def start(self):
        """
        Starts the Game of Life
        """
        self.refresh_screen()
        continue_execution = True
        while continue_execution:
            input_key = self.screen.get_input_key()
            continue_execution = self.dispatch_user_command(input_key)

    def dispatch_user_command(self, input_key):
        """
        Takes a user input and decides what to do about it
        """
        # Dispatch command to the current mode
        self._mode.dispatch_user_command(self, input_key)
        # Common commands for all Modes
        if input_key == Command.QUIT:
            return False
        elif input_key == Command.INSERT_MODE:
            self.mode = Mode.INSERT
        elif input_key == Command.NORMAL_MODE:
            self.mode = Mode.NORMAL
        elif input_key == Command.PAN_MODE:
            self.mode = Mode.PAN
        elif input_key == Command.RECORD_MODE:
            self.mode = Mode.RECORD
        elif input_key == Command.REPLAY_MODE:
            self.mode = Mode.REPLAY
        elif input_key == Command.INSERT_CELL:
            self.add_cell(self.screen.cursor_position)
        elif input_key == Command.DELETE_CELL:
            self.remove_cell(self.screen.cursor_position)
        elif input_key == Command.SAVE_BOARD:
            self.save()
        elif input_key == Command.LOAD_BOARD:
            self.load()

        return True

    def add_cell(self, position):
        self.board.add_cell(position)
        self.screen.add_cell(position)

    def remove_cell(self, position):
        self.board.remove_cell(position)
        self.screen.remove_cell(position)

    def refresh_screen(self):
        self.screen.save_cursor()
        self.screen.clear()
        for point in self.board.cells:
            self.screen.add_cell(point)
        self.screen.restore_cursor()

    def step(self):
        self.board.step()
        self.refresh_screen()

    def replay_step(self):
        if not hasattr(self, "replay_fhandle"):
            self.replay_fhandle = open(self.REPLAY_FILENAME)
        try:
            serialized_board_state = self.replay_fhandle.readline()
            self.board.load_serialized_board(serialized_board_state)
            self.refresh_screen()
        except:
            return

    def save(self):
        with open(self.SAVE_FILENAME, mode='w') as save_fhandle:
            board_state = self.board.serialize_board()
            save_fhandle.write(board_state)

    def load(self):
        with open(self.SAVE_FILENAME) as save_fhandle:
            serialized_board_state = save_fhandle.readline()
            self.board.load_serialized_board(serialized_board_state)
        self.refresh_screen()

    def record(self):
       with open(self.RECORD_FILENAME, mode='a') as record_fhandle:
            board_state = self.board.serialize_board()
            record_fhandle.write(board_state + '\n')


if __name__ == '__main__':
    curses.wrapper(GameOfLife)

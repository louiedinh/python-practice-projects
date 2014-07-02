import json

from datastructures import Vector, Point


class Board:
    """ 
    A game board that tracks all living cells
    cell_positions is a map keyed by Point objects
    """
    NEIGHBOUR_TRANFORMS = [Vector(-1, -1), Vector(-1, 0), Vector(-1, 1), 
                           Vector(0, -1), Vector(0, 1),
                           Vector(1, -1),  Vector(1, 0), Vector(1, 1)]

    def __init__(self, initial_positions=[]):
        self.cell_positions = {}
        for p in initial_positions:
           self.add_cell(p)

    @property
    def cells(self):
        return self.cell_positions.keys()

    @property
    def cell_count(self):
        return len(self.cell_positions)
 
    @property
    def empty_neighbour_set(self):
        all_neighbours = [Point(p.row+v.row, p.col+v.col) for p in self.cells for v in Board.NEIGHBOUR_TRANFORMS] 
        return set([n for n in all_neighbours if not self.cell_at(n)])

    def cell_at(self, point):
        return self.cell_positions.get(point, False)

    def add_cell(self, point) -> bool:
        """
        Add a cell at <point> :: Point.
        Returns:
            True on success
            False otherwise
        """
        if not self.cell_at(point):
            self.cell_positions[point] = True
            return True
        else:
            return False

    def remove_cell(self, point) -> bool:
        """
        Remove the cell at point :: Point.
        Returns:
            True on success
            False otherwise
        """
        if self.cell_at(point):
            del self.cell_positions[point]
            return True
        else:
            return False

    def live_neighbours_count(self, point):
        all_neighbours = [Point(point.row+v.row, point.col+v.col) for v in Board.NEIGHBOUR_TRANFORMS] 
        return len([n for n in all_neighbours if self.cell_at(n)])
   
    def step(self):
        # Create a new empty board
        next_cell_positions = {}
        # For each live cell: 2/3 neighbours = live. Else die.
        for cell_position in self.cells:
            neighbour_count = self.live_neighbours_count(cell_position)
            if neighbour_count == 2 or neighbour_count == 3:
                next_cell_positions[cell_position] = True
        # For each empty plot: 3 live neighbours = live. Else same.
        for empty_position in self.empty_neighbour_set:
            neighbour_count = self.live_neighbours_count(empty_position)
            if neighbour_count == 3:
                next_cell_positions[empty_position] = True 
        self.cell_positions = next_cell_positions

    def serialize_board(self):
        """
        Returns a string representing the board state
        """
        listified_cell_positions = {"{0},{1}".format(position.row, position.col): value for (position,value) in self.cell_positions.items()}
        return json.dumps(listified_cell_positions)

    def load_serialized_board(self, serialized_board):
        """ 
        Loads a serialized board and overwrites the current board.
        """
        self.cell_positions = {}
        deserialized_board = json.loads(serialized_board)
        for position_str, value in deserialized_board.items():
            row, col = [int(x) for x in position_str.split(',')]
            self.add_cell(Point(row=row, col=col))



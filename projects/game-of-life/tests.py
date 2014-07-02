import unittest

from game_of_life import *

class BoardTestCase(unittest.TestCase):

    def setUp(self):
        self.initial_coordinates = [(1,1), (2,2), (3,3)]
        self.initial_positions = [Point(x,y) for x,y in self.initial_coordinates]
        self.board = Board(self.initial_positions)

    def test_init(self):
        # Check that all the initial positions are filled
        for x,y in self.initial_coordinates:
            self.assertTrue(self.board.cell_at(Point(x,y)))
        # Check that they are the only ones filled
        self.assertEqual(len(self.board.cell_positions), len(self.initial_coordinates))

    def test_add_cell(self):
        p = Point(100,100)
        self.board.add_cell(p)
        self.assertTrue(self.board.cell_at(p))
        self.assertEqual(self.board.cell_count, len(self.initial_positions) + 1)

    def test_remove_cell(self):
        self.board.remove_cell(Point(1,1))
        self.assertFalse(self.board.cell_at(Point(1,1)))
        self.assertEqual(self.board.cell_count, len(self.initial_positions) - 1)

    def test_cell_at(self):
        for x,y in self.initial_coordinates:
            self.assertTrue(self.board.cell_at(Point(x,y)))

    def test_cell_count(self):
        self.assertEqual(len(self.initial_positions), self.board.cell_count)

    def test_get_empty_neighbour_set(self):
        self.initial_coordinates = [(1,1), (2,2)]
        self.initial_positions = [Point(x,y) for x,y in self.initial_coordinates]
        self.board = Board(self.initial_positions)
        expected_empty_neighbours_set = set([Point(row=0, col=1), Point(row=1, col=2), Point(row=3, col=2), Point(row=0, col=0),
                                             Point(row=3, col=3), Point(row=3, col=1), Point(row=2, col=1), Point(row=2, col=0),
                                             Point(row=1, col=3), Point(row=2, col=3), Point(row=1, col=0), Point(row=0, col=2)])
        self.assertEqual(expected_empty_neighbours_set, self.board.empty_neighbour_set)

    def test_live_neighbours_count(self):
        self.assertEqual(self.board.live_neighbours_count(Point(1,1)), 1)
        self.assertEqual(self.board.live_neighbours_count(Point(2,2)), 2)
        self.assertEqual(self.board.live_neighbours_count(Point(3,3)), 1)
        
if __name__ == '__main__':
    unittest.main()

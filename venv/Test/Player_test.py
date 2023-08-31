# test_player.py
import unittest
from App.Player import Player

class TestPlayerValues(unittest.TestCase):

    # Expected to fail test
    def test_name(self):
        player = Player(uid=123, name='Alice')
        self.assertEqual(player.name, 'Jesus', 'The names do not match.')

    # Expected to pass test
    def test_uid(self):
        player = Player(uid=132, name='Alice')
        self.assertEqual(player.uid, 132, 'The uid does not match.')

    # Expected to pass test
    def test_nameTwo(self):
        player = Player(uid=132, name='Alice')
        self.assertEqual(player.name, 'Alice', 'The names do not match.')

if __name__ == '__main__':
    unittest.main()
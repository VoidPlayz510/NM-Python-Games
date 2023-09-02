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

    def test_passwords_first(self):
        player = Player(1, name="Bob")

        # set password
        player.add_password("MyPassword")
        self.assertTrue(player.verify_password("MyPassword"))
        self.assertFalse(player.verify_password("NotMyPassword"))


    def test_passwords_second(self):
        player = Player(2, name="Bandy")

        # set password
        player.add_password("MyPasswordTwo")
        self.assertTrue(player.verify_password("MyPasswordTwo"))
        self.assertFalse(player.verify_password("NotMyPasswordTwo"))

if __name__ == '__main__':
    unittest.main()
import unittest
from src.app.player import Player


class TestPlayerValues(unittest.TestCase):
    """
    Unit tests for the Player class.
    """

    def test_name(self):
        """
        Test the player's name.
        """
        player = Player(uid=123, name='Alice')
        self.assertEqual(player.name, 'Alice', 'The names do not match.')

    def test_uid(self):
        """
        Test the player's UID.
        """
        player = Player(uid=132, name='Alice')
        self.assertEqual(player.uid, 132, 'The UID does not match.')

    def test_passwords_first(self):
        """
        Test setting and verifying a player's password.
        """
        player = Player(1, name="Bob")

        player.add_password("MyPassword")
        self.assertTrue(player.verify_password("MyPassword"))
        self.assertFalse(player.verify_password("NotMyPassword"))

    def test_passwords_second(self):
        """
        Test setting and verifying another player's password.
        """
        player = Player(2, name="Bandy")

        player.add_password("MyPasswordTwo")
        self.assertTrue(player.verify_password("MyPasswordTwo"))
        self.assertFalse(player.verify_password("NotMyPasswordTwo"))


if __name__ == '__main__':
    unittest.main()

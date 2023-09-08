import unittest
from app.player import Player


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

    def test_player_operators(self):
        """
        Testing operators such as:
        ==
        >=
        <=
        <
        >
        """
        player1 = Player(1, "Alice")
        player1.score = 100

        player2 = Player(2, "Bob")
        player2.score = 150

        self.assertTrue(player1 < player2)
        self.assertFalse(player1 > player2)
        self.assertTrue(player1 <= player2)
        self.assertTrue(player2 > player1)
        self.assertTrue(player2 >= player1)
        self.assertTrue(player1 != player2)

    def test_sort_score(self):
        Player.clear_list()

        player1 = Player(1, "Alice")
        player1.score = 23

        player2 = Player(2, "Bob")
        player2.score = 150

        player3 = Player(3, "John")
        player3.score = 53

        player3 = Player(4, "Mary")
        player3.score = 173

        player4 = Player(5, "Park")
        player4.score = 102

        player_list = Player.sort_list(Player._player_list)
        test_list = [173, 150, 102, 53, 23]

        self.assertEqual(player_list, test_list, 'The list is not the same')
        print(player_list)


if __name__ == '__main__':
    unittest.main()

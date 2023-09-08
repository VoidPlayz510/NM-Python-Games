import unittest
from app.player import Player
from app.player_list import PlayerList


def get_last_player_name(player_list):
    """
    Get the name of the last player in the player list.

    :param player_list: The PlayerList object.
    :return: The name of the last player.
    """
    return player_list.players[-1].name


class TestPlayerList(unittest.TestCase):
    """
    Unit tests for the PlayerList class.
    """

    def test_push_front(self):
        """
        Test pushing a player to the front of the list.
        """
        player_list = PlayerList()
        player1 = Player(1, name='Player 1')
        player2 = Player(2, name='Player 2')

        player_list.push_front(player1)
        player_list.push_front(player2)

        self.assertEqual(player_list.head.player, player2)
        self.assertEqual(player_list.tail.player, player1)

    def test_push_front_empty_list(self):
        """
        Test pushing a player to the front of an empty list.
        """
        player_list = PlayerList()
        player = Player(1, name='Player')

        player_list.push_front(player)

        self.assertEqual(player_list.head.player, player)
        self.assertEqual(player_list.tail.player, player)

    def test_push_front_multiple_players(self):
        """
        Test pushing multiple players to the front of the list.
        """
        player_list = PlayerList()
        player1 = Player(1, name='Player 1')
        player2 = Player(2, name='Player 2')
        player3 = Player(3, name='Player 3')

        player_list.push_front(player1)
        player_list.push_front(player2)
        player_list.push_front(player3)

        self.assertEqual(player_list.head.player, player3)
        self.assertEqual(player_list.tail.player, player1)

    def test_empty_list(self):
        """
        Test checking if the list is empty.
        """
        player_list = PlayerList()

        self.assertTrue(player_list.is_empty())

    def test_push_tail(self):
        """
        Test pushing a player to the end of the list.
        """
        player_list = PlayerList()
        player1 = Player(1, name='Player 1')
        player2 = Player(2, name='Player 2')
        player3 = Player(3, name='Player 3')

        player_list.push_front(player2)
        player_list.push_end(player3)
        player_list.push_end(player1)

        last_player = player_list.peek_back()

        self.assertEqual(last_player.name, 'Player 1', 'The player\'s do not match')

    def test_pop_front(self):
        """
        Test popping a player from the front of the list.
        """
        player_list = PlayerList()
        player1 = Player(1, name='Player 1')
        player2 = Player(2, name='Player 2')
        player_list.push_front(player1)
        player_list.push_front(player2)

        front_player_before = player_list.peek_front()
        self.assertEqual(front_player_before, player2)

        popped_player = player_list.pop_front()
        self.assertEqual(popped_player, player2)

        front_player_after = player_list.peek_front()
        self.assertEqual(front_player_after, player1)

    def test_pop_tail(self):
        """
        Test popping a player from the end of the list.
        """
        player_list = PlayerList()
        player1 = Player(1, name='Player 1')
        player2 = Player(2, name='Player 2')
        player_list.push_front(player1)
        player_list.push_front(player2)

        back_player_tail = player_list.peek_back()
        self.assertEqual(back_player_tail, player1)

        popped_player = player_list.pop_end()
        self.assertEqual(popped_player, player1)
        front_player_after = player_list.peek_front()
        self.assertEqual(front_player_after, player2)

    def test_pop_end_empty_list(self):
        """
        Test popping a player from an empty list.
        """
        player_list = PlayerList()

        popped_player = player_list.pop_end()

        self.assertIsNone(popped_player)
        self.assertIsNone(player_list.head)
        self.assertIsNone(player_list.tail)

    def test_pop_key(self):
        """
        Test popping a player by their UID.
        """
        player_list = PlayerList()

        player1 = Player(1, name="Player 1")
        player2 = Player(2, name="Player 2")
        player3 = Player(3, name="Player 3")

        player_list.push_front(player1)
        player_list.push_front(player2)
        player_list.push_end(player3)

        player_list.pop_key(2)

        self.assertEqual(player_list.head._player.uid, 1)
        self.assertEqual(player_list.tail._player.uid, 3)

    def test_forward_display(self):
        """
        Test displaying the list in forward order.
        """
        predefined_list = PlayerList()
        player1 = Player(1, name="Player 1")
        player2 = Player(2, name="Player 2")
        player3 = Player(3, name="Player 3")
        predefined_list.push_front(player1)
        predefined_list.push_front(player2)
        predefined_list.push_front(player3)

        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output

        predefined_list.display_list(forward=True)

        sys.stdout = sys.__stdout__

        printed_output = captured_output.getvalue().strip().split('\n')
        expected_output = [
            "Player ID: 3, Name: Player 3",
            "Player ID: 2, Name: Player 2",
            "Player ID: 1, Name: Player 1",
        ]
        self.assertEqual(printed_output, expected_output)

        print("\nLList Output:")
        print("\n".join(printed_output))

    def test_backwards_display(self):
        """
        Test displaying the list in reverse order.
        """
        predefined_list = PlayerList()
        player1 = Player(1, name="Player 1")
        player2 = Player(2, name="Player 2")
        player3 = Player(3, name="Player 3")
        predefined_list.push_front(player1)
        predefined_list.push_front(player2)
        predefined_list.push_front(player3)

        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output

        predefined_list.display_list(forward=False)

        sys.stdout = sys.__stdout__

        printed_output = captured_output.getvalue().strip().split('\n')
        expected_output = [
            "Player ID: 1, Name: Player 1",
            "Player ID: 2, Name: Player 2",
            "Player ID: 3, Name: Player 3",
        ]
        self.assertEqual(printed_output, expected_output)

        print("\nLList Output:")
        print("\n".join(printed_output))


if __name__ == '__main__':
    unittest.main()

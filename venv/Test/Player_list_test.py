# test_player_list.py
import unittest
from App.Player_list import PlayerList
from App.Player_node import PlayerNode  # Import the PlayerNode class from player_node.py
from App.Player import Player  # Import the Player class from the appropriate location

class TestPlayerList(unittest.TestCase):

    def test_push_front(self):
        player_list = PlayerList()
        player1 = Player(1, name='Player 1')
        player2 = Player(2, name='Player 2')

        player_list.push_front(player1)
        player_list.push_front(player2)


        # Pushing player 1 and then 2 should make player 1 the end time and player 2
        # the new top item
        self.assertEqual(player_list.head.player, player2)
        self.assertEqual(player_list.tail.player, player1)


    # Pushing from an empty list should have the head and tail as the same item
    # as there is only one player anyway
    def test_push_front_empty_list(self):
        player_list = PlayerList()
        player = Player(1, name='Player')

        player_list.push_front(player)

        self.assertEqual(player_list.head.player, player)
        self.assertEqual(player_list.tail.player, player)


    # test with multiple players for head and tail (front/back)
    def test_push_front_multiple_players(self):
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
        player_list = PlayerList()

        self.assertTrue(player_list.is_empty())

    def get_last_player_name(self, player_list):
        return player_list.players[-1].name

    def test_push_tail(self):
        player_list = PlayerList()
        player1 = Player(1, name='Player 1')
        player2 = Player(2, name='Player 2')
        player3 = Player(3, name='Player 3')

        player_list.push_front(player2)
        player_list.push_end(player3)
        player_list.push_end(player1)

        last_player = player_list.peek_back()

        self.assertEqual(last_player.name, 'Player 1', 'The player\'s do not match')

if __name__ == '__main__':
    unittest.main()
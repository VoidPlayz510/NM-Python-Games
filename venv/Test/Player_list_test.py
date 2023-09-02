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

    def test_pop_front(self):
        # Create a PlayerList and add some players
        player_list = PlayerList()
        player1 = Player(1, name='Player 1')
        player2 = Player(2, name='Player 2')
        player_list.push_front(player1)
        player_list.push_front(player2) # last item pushed up

        # Check if the front player is the one expected before popping
        front_player_before = player_list.peek_front()
        self.assertEqual(front_player_before, player2)  # Assert that player2 is the front player

        # Pop the front player
        popped_player = player_list.pop_front() # player2 is now gone

        # Check if the popped player is the one we expected (player2)
        self.assertEqual(popped_player, player2)

        # Check if the front player is now the one expected (player1)
        front_player_after = player_list.peek_front()
        self.assertEqual(front_player_after, player1)


    def test_pop_tail(self):
        # Create a PlayerList and add some players
        player_list = PlayerList()
        player1 = Player(1, name='Player 1')
        player2 = Player(2, name='Player 2')
        player_list.push_front(player1)
        player_list.push_front(player2)

        # Check if the front player is the one expected before popping
        back_player_tail = player_list.peek_back()
        self.assertEqual(back_player_tail, player1)  # Assert that player1 is the back player

        # Pop the back player
        popped_player = player_list.pop_end() # player1 is now gone

        # Check if the popped player is the one we expected (player1)
        self.assertEqual(popped_player, player1)

        # Check if the front player is now the one expected (player2)
        front_player_after = player_list.peek_front()
        self.assertEqual(front_player_after, player2)

    def test_pop_end_empty_list(self):
        player_list = PlayerList()

        # Attempt to pop from an empty/null list
        popped_player = player_list.pop_end()

        # Check if the popped_player is None, an empty list
        self.assertIsNone(popped_player)

        # Check if the list is still empty (both head and tail should be None)
        self.assertIsNone(player_list.head)
        self.assertIsNone(player_list.tail)
if __name__ == '__main__':
    unittest.main()
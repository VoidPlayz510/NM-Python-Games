import unittest
from app.player import Player
from app.player_bnode import PlayerBNode
from app.player_bst import PlayerBST


class TestPlayerValues(unittest.TestCase):
    """
    Unit tests for the Player class.
    """

    def test_player_name_matches_expected(self):
        """
        Test that the player's name matches the expected name.
        """
        player = Player(uid=123, name='Alice')
        self.assertEqual(player.name, 'Alice', 'The names do not match.')

    def test_player_uid_matches_expected(self):
        """
        Test that the player's UID matches the expected UID.
        """
        player = Player(uid=132, name='Alice')
        self.assertEqual(player.uid, 132, 'The UIDs do not match.')

    def test_player_password_set_and_verify(self):
        """
        Test setting and verifying a player's password.
        """
        player = Player(1, name="Bob")

        player.add_password("MyPassword")
        self.assertTrue(player.verify_password("MyPassword"))
        self.assertFalse(player.verify_password("NotMyPassword"))

    def test_another_player_password_set_and_verify(self):
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
        """
        Test that the score values are being correctly sorted
        """
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

    def test_insert_empty_tree(self):
        """
        Test sucessfully inserting into an empty BST
        """
        bst = PlayerBST()

        self.assertTrue(bst.is_empty())
        player1 = Player(1, "Alice")

        bst.insert(player1)

        self.assertFalse(bst.is_empty())
        self.assertEqual(bst.root.key, "Alice")

    def test_insert_into_non_empty_tree_and_check_left_child(self):
        """
        Check if the BST is empty and check the left node to see if it's correctly placed
        """
        bst = PlayerBST()

        player1 = Player(1, "Alice")
        player2 = Player(2, "Bob")
        player3 = Player(3, "Charlie")

        bst.insert(player1)
        bst.insert(player2)
        bst.insert(player3)

        self.assertFalse(bst.is_empty())
        self.assertEqual(bst.root.key, "Alice")

        if bst.root.left:
            left_child = bst.root.left
            self.assertEqual(left_child.key, "Alice")

    def test_insert_into_non_empty_tree_and_check_right_child(self):
        """
        Check if the BST is empty and check the right node to see if it's correctly placed
        """
        bst = PlayerBST()

        player1 = Player(1, "Alice")
        player2 = Player(2, "Bob")
        player3 = Player(3, "Charlie")

        bst.insert(player1)
        bst.insert(player2)
        bst.insert(player3)

        self.assertFalse(bst.is_empty())
        self.assertEqual(bst.root.key, "Alice")

        if bst.root.right:
            right_child = bst.root.right
            self.assertEqual(right_child.key, "Bob")

    def test_search_get_player_name(self):
        """
        Test the ability to get a player in the BST from its name
        """
        bst = PlayerBST()

        player1 = Player(1, "Alice")
        player2 = Player(2, "Bob")
        player3 = Player(3, "Charlie")

        bst.insert(player1)
        bst.insert(player2)
        bst.insert(player3)

        searched_player = bst.search("Bob")

        self.assertIsNotNone(searched_player)
        self.assertEqual(searched_player.key, "Bob")

    def test_unsorted_bst_to_balanced_bst(self):
        """
        Test creating an unsorted BST and reorder it to a balanced BST
        """
        bst = PlayerBST()

        player1 = Player(1, "Alice")
        player2 = Player(2, "Bob")
        player3 = Player(3, "Charlie")

        bst.insert(player1)
        bst.insert(player2)
        bst.insert(player3)

        bst.create_balanced_bst()

        self.assertTrue(bst.is_balanced())


if __name__ == '__main__':
    unittest.main()

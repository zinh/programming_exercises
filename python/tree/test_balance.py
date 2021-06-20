import unittest
from tree import Node
from balance import Solution


class TestBalance(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_none(self):
        self.assertTrue(self.solution.isBalanced(None))

    def test_balance(self):
        tree = Node(3, Node(9), Node(20, Node(15), Node(7)))
        self.assertTrue(self.solution.isBalanced(tree))

    def test_unbalance(self):
        tree = Node(1, Node(2, Node(3, Node(4), Node(4)), Node(3)), Node(2))
        self.assertFalse(self.solution.isBalanced(tree))

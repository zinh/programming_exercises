import unittest
from tree import Node
from depth import Solution


class TestDepth(unittest.TestCase):
    def test_empty_tree(self):
        solution = Solution()
        self.assertEqual(0, solution.maxDepth(None))

    def test_normal_tree(self):
        solution = Solution()
        self.assertEqual(2, solution.maxDepth(Node(1, None, Node(2))))

        tree2 = Node(3, Node(9), Node(20, Node(15), Node(7)))
        self.assertEqual(3, solution.maxDepth(tree2))

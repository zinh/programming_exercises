import unittest
from symetric_tree import Solution
from tree import Node


class TestSymetricTree(unittest.TestCase):
    def test_symetric_tree(self):
        solution = Solution()
        #        1
        #     /     \
        #    2       2
        #  /   \   /   \
        # 3     4 4     3
        tree = Node(1,
                    Node(2, Node(3), Node(4)),
                    Node(2, Node(4), Node(3))
                    )
        self.assertTrue(solution.isSymmetric(tree))

    def test_asymetric_tree(self):
        solution = Solution()
        #      1
        #    /   \
        #   2     2
        #    \     \
        #     3     3
        tree = Node(1, Node(2, None, Node(3)), Node(2, None, Node(3)))
        self.assertFalse(solution.isSymmetric(tree))

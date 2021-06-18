import unittest
from tree import Node
from same_tree import is_same_tree


class TestSameTree(unittest.TestCase):
    def test_normal_case(self):
        tree1 = Node(1, Node(2), Node(3))
        tree2 = Node(1, Node(2), Node(3))
        self.assertEqual(True, is_same_tree(tree1, tree2))

    def test_none_node(self):
        tree1 = Node(1)
        self.assertEqual(True, is_same_tree(None, None))
        self.assertEqual(False, is_same_tree(tree1, None))
        self.assertEqual(False, is_same_tree(None, tree1))

    def test_not_same_tree(self):
        tree1 = Node(1)
        tree2 = Node(2)
        self.assertEqual(False, is_same_tree(tree1, tree2))

        tree1 = Node(1, Node(2), Node(3))
        tree2 = Node(1, Node(2), Node(4))
        self.assertEqual(False, is_same_tree(tree1, tree2))

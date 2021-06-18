import unittest
from inorder import TreeNode, Solution

class InorderTest(unittest.TestCase):
    def test_inorder(self):
        solution = Solution()
        tree = TreeNode(1, None, TreeNode(2, TreeNode(3)))

class Solution:
    def maxDepth(self, root) -> int:
        if root is None:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1

    def isBalanced(self, root) -> bool:
        if root is None:
            return True
        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)
        return self.isBalanced(root.left) \
            and self.isBalanced(root.right) \
            and abs(right_height - left_height) <= 1

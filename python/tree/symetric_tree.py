class Solution:
    def isSymmetric(self, root) -> bool:
        if root is None:
            return True
        return self.isSymetricTree(root.left, root.right)

    def isSymetricTree(self, left, right) -> bool:
        if left is None or right is None:
            if left == right:
                return True
            else:
                return False
        if left.val == right.val:
            return self.isSymetricTree(left.right, right.left) and self.isSymetricTree(left.left, right.right)
        else:
            return False

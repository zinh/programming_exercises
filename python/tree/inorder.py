from typing import List
from queue import Queue, LifoQueue

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)

    @property
    def height(self):
        left_height = 0 if self.left is None else self.left.height
        right_height = 0 if self.right is None else self.right.height
        return max(left_height, right_height) + 1

    # left, root, right
    def inorder(self):
        left = [] if self.left is None else self.left.inorder()
        right = [] if self.right is None else self.right.inorder()
        return left + [self.val] + right

    def inorder_iter(self):
        stack = LifoQueue()
        stack.put(self)
        result = []
        while not stack.empty():
            item = stack.get()
            if item is None:
                continue
            if item.left is None:
                result.append(item.val)
            else:
                stack.put(item)
                stack.put(item.left)
            stack.put(item.right)
        return result

    # root, left, right
    def preorder(self):
        left = [] if self.left is None else self.left.preorder()
        right = [] if self.right is None else self.right.preorder()
        return [self.val] + left + right

    # left, right, root
    def postorder(self):
        left = [] if self.left is None else self.left.postorder()
        right = [] if self.right is None else self.right.postorder()
        return left + right + [self.val]

    def level_order(self):
        result = [self.val]
        subtree = []
        if self.left is not None:
            result.append(self.left.val)
            subtree += self.left.level_order()[1:]
        if self.right is not None:
            result.append(self.right.val)
            subtree += self.right.level_order()[1:]
        return result + subtree

    def level_order_iter(self):
        queue = Queue()
        result = []
        queue.put(self)
        while not queue.empty():
            item = queue.get()
            if item is None:
                continue
            result.append(item.val)
            queue.put(item.left)
            queue.put(item.right)
        return result

    def leaf_travesal(self):
        pass

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        pass

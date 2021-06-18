def is_same_tree(tree1, tree2):
    if tree1 is None or tree2 is None:
        if tree1 == tree2:
            return True
        else:
            return False

    if tree1.val == tree2.val:
        return is_same_tree(tree1.left, tree2.left) and is_same_tree(tree1.right, tree2.right)
    return False

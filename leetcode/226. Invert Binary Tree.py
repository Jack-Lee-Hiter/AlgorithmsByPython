'''
Invert a binary tree.

     4
   /   \
  2     7
 / \   / \
1   3 6   9
to
     4
   /   \
  7     2
 / \   / \
9   6 3   1
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def invertTree(self, root):
        if not root:
            return
        if not root.left and not root.right:
            return root
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

    def invertTree2(self, root):
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root
    # interative
    def invertTreeInter(self, root):
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stack += node.left, node.right
        return root

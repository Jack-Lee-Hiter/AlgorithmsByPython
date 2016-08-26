'''
Given inorder and postorder traversal of a tree, construct the binary tree.
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        if not inorder or not postorder:
            return None

        root = TreeNode(postorder.pop())
        ind = inorder.index(root.val)

        root.right = self.buildTree(inorder[ind + 1:], postorder)
        root.left = self.buildTree(inorder[:ind], postorder)
        return root

    # method2, faster!!
    def buildTree2(self, inorder, postorder):
        self.postInd = len(postorder) - 1
        ind = {val: ind for ind, val in enumerate(inorder)}
        head = self.build(0, len(postorder) - 1, inorder, postorder, ind)
        return head

    def build(self, start, end, inorder, postorder, ind):
        if start <= end:
            mid = ind[postorder[self.postInd]]
            self.postInd -= 1
            root = TreeNode(inorder[mid])
            root.right = self.build(mid + 1, end, inorder, postorder, ind)
            root.left = self.build(start, mid - 1, inorder, postorder, ind)
            return root

s = Solution()
print(s.buildTree2([1,2,3,4],[2,4,3,1]))
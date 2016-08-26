'''
Given preorder and inorder traversal of a tree, construct the binary tree.
'''
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # recursion
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return
        root = TreeNode(preorder[0])
        ind = inorder.index(preorder.pop(0))
        root.left = self.buildTree(preorder, inorder[0:ind])
        root.right = self.buildTree(preorder, inorder[ind + 1:])
        return root
    # method2, faster!!
    def buildTree2(self, preorder, inorder):
        self.Ind = 0
        ind = {val: ind for ind, val in enumerate(inorder)}
        head = self.build(0, len(preorder) - 1, preorder, inorder, ind)
        return head

    def build(self, start, end, preorder, inorder, ind):
        if start <= end:
            mid = ind[preorder[self.Ind]]
            self.Ind += 1
            root = TreeNode(inorder[mid])
            root.left = self.build(start, mid - 1, preorder, inorder, ind)
            root.right = self.build(mid + 1, end, preorder, inorder, ind)
            return root
    # Interative
    def buildTreeInter(self, preorder, inorder):
        if len(preorder) == 0:
            return None

        head = TreeNode(preorder[0])
        stack = [head]
        preInd, inInd = 1, 0

        while preInd < len(preorder):
            temp = None
            node = TreeNode(preorder[preInd])
            while stack and stack[-1].val == inorder[inInd]:
                temp = stack.pop()
                inInd += 1
            if temp:
                temp.right = node
            else:
                stack[-1].left = node
            stack.append(node)
            preInd += 1

        return head
'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
'''

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # recursive
    def isSymmetric(self, root):
        return self._Symmetrical(root, root)
    def _Symmetrical(self, pRoot1, pRoot2):
        if pRoot1 and pRoot2:
            return pRoot1.val == pRoot2.val and self._Symmetrical(pRoot1.left, pRoot2.right) and self._Symmetrical(
                pRoot1.right, pRoot2.left)
        else:
            return pRoot1 == pRoot2

    #iterative(BFS)
    def isSymmetric2(self, root):
        if root:
            now = [root]
            while now:
                vals = [i.val if i else None for i in now]
                if list(reversed(vals)) != vals:
                    return False
                else:
                    now = [j for i in now if i for j in (i.left, i.right)]
        return True
    # modify iterative(BFS)
    def isSymmetric_2(self, root):
        if root:
            nodeStack = [root]
            while nodeStack:
                vals = [node.val if node else None for node in nodeStack]
                if list(reversed(vals)) != vals:
                    return False
                else:
                    preStack = [node for node in nodeStack if node]
                    nodeStack = []
                    for preNode in preStack:
                        nodeStack.append(preNode.left)
                        nodeStack.append(preNode.right)
        return True

    # iterative(DFS)
    def isSymmetric3(self, root):
        if root:
            stack = [(root.left, root.right)]
            while len(stack) > 0:
                p, q = stack.pop()
                if p and q and p.val == q.val:
                    stack.append((p.left, q.right))
                    stack.append((p.right, q.left))
                elif p != q:
                    return False
        return True


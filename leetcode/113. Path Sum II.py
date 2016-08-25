'''
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        if not root:
            return []
        if root.left == None and root.right == None:
            if sum == root.val:
                return [[root.val]]
            else:
                return []
        stack = []
        leftStack = self.pathSum(root.left, sum - root.val)
        for i in leftStack:
            i.insert(0, root.val)
            stack.append(i)
        rightStack = self.pathSum(root.right, sum - root.val)
        for i in rightStack:
            i.insert(0, root.val)
            stack.append(i)
        return stack

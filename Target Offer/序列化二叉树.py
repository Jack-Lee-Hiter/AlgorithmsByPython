'''
请实现两个函数，分别用来序列化和反序列化二叉树。这里没有规定序列化的方式。
'''

# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Serialize(self, root):
        serializeStr = ''
        if root == None:
            return '#'
        stack = []
        while root or stack:
            while root:
                serializeStr += str(root.val) + ','
                stack.append(root)
                root = root.left
            serializeStr += '#,'
            root = stack.pop()
            root = root.right
        serializeStr = serializeStr[:-1]
        return serializeStr

    def Deserialize(self, s):
        serialize = s.split(',')
        tree, sp = self.deserialize(serialize, 0)
        return tree

    def deserialize(self, s, sp):
        if sp >= len(s) or s[sp] == '#':
            return None, sp + 1
        node = TreeNode(int(s[sp]))
        sp += 1
        node.left, sp = self.deserialize(s, sp)
        node.right, sp = self.deserialize(s, sp)
        return node, sp
'''
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

For example, you may serialize the following tree

    1
   / \
  2   3
     / \
    4   5
as "[1,2,3,null,null,4,5]"
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        if not root:
            return 'None'
        stack, seriStr = [], ""
        while root or stack:
            while root:
                seriStr += str(root.val) + ','
                stack.append(root)
                root = root.left
            seriStr += 'None,'
            root = stack.pop()
            root = root.right
        seriStr = seriStr[:-1]
        return seriStr

    def deserialize(self, data):
        serialize = data.split(',')
        tree, sp = self.bulidTree(serialize, 0)
        return tree

    def bulidTree(self, s, sp):
        if sp >= len(s) or s[sp] == 'None':
            return None, sp + 1
        node = TreeNode(int(s[sp]))
        sp += 1
        node.left, sp = self.bulidTree(s, sp)
        node.right, sp = self.bulidTree(s, sp)
        return node, sp
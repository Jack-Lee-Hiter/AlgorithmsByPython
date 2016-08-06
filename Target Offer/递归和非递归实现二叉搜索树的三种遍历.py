# -*- coding:UTF-8 -*-
'''
利用递归以及非递归的方式实现二叉搜索树的前序遍历、中序遍历和后序遍历
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Tranversal:
    # preorder without recursion
    def preOrder(self, root):
        if root == None:
            return None
        pNode, treeStack = root, []
        while pNode or len(treeStack) > 0:
            while pNode:
                print(pNode.val)
                treeStack.append(pNode)
                pNode = pNode.left
            if len(treeStack) > 0:
                pNode = treeStack.pop()
                pNode = pNode.right
    # preorder with recursion
    def preOrderRec(self, root):
        if root != None:
            print(root.val)
            self.preOrderRec(root.left)
            self.preOrderRec(root.right)
    # inorder without recursion
    def inOrder(self, root):
        if root == None:
            return
        pNode, treeStack = root, []
        while pNode or len(treeStack) > 0:
            while pNode:
                treeStack.append(pNode)
                pNode = pNode.left
            if len(treeStack) > 0:
                pNode = treeStack.pop()
                print(pNode.val)
                pNode = pNode.right
    # inorder with recursion
    def inOrderRec(self, root):
        if root != None:
            self.inOrderRec(root.left)
            print(root.val)
            self.inOrderRec(root.right)
    # postorder without recursion
    def postOrder(self, root):
        if root == None:
            return
        cur, pre, treeStack = root, None, []  # cur:current Node, pre: pre visited Node
        treeStack.append(root)
        while len(treeStack) > 0:
            cur = treeStack[-1]
            # current node doesn't have child nodes or child nodes have been visited
            if (cur.left == None and cur.right == None) or (pre != None and (pre == cur.left or pre == cur.right)):
                print(cur.val)
                pre = treeStack.pop()
            else:
                if cur.right != None:
                    treeStack.append(cur.right)
                if cur.left != None:
                    treeStack.append(cur.left)
    # postorder with cursion
    def postOrderRec(self, root):
        if root:
            self.postOrderRec(root.left)
            self.postOrderRec(root.right)
            print(root.val)

pNode1 = TreeNode(10)
pNode2 = TreeNode(6)
pNode3 = TreeNode(14)
pNode4 = TreeNode(4)
pNode5 = TreeNode(8)
pNode6 = TreeNode(12)
pNode7 = TreeNode(16)

pNode1.left = pNode2
pNode1.right = pNode3
pNode2.left = pNode4
pNode2.right = pNode5
pNode3.left = pNode6
pNode3.right = pNode7

S = Tranversal()
S.postOrder(pNode1)
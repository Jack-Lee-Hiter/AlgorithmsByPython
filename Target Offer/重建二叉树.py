'''
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
'''

# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if not pre and not tin:
            return None
        root = TreeNode(pre[0])
        if set(pre) != set(tin):
            return None
        i = tin.index(pre[0])
        root.left = self.reConstructBinaryTree(pre[1:i+1], tin[:i])
        root.right = self.reConstructBinaryTree(pre[i+1:], tin[i+1:])
        return root

pre = [1, 2, 3, 5, 6, 4]
tin = [5, 3, 6, 2, 4, 1]
test = Solution()
newTree = test.reConstructBinaryTree(pre, tin)
# 按层序遍历输出树中某一层的值
def PrintNodeAtLevel(treeNode, level):
    if not treeNode or level < 0:
        return 0
    if level == 0:
        print(treeNode.val)
        return 1
    PrintNodeAtLevel(treeNode.left, level-1)
    PrintNodeAtLevel(treeNode.right, level-1)

# 已知树的深度按层遍历输出树的值
def PrintNodeByLevel(treeNode, depth):
    for level in range(depth):
        PrintNodeAtLevel(treeNode, level)

# # 不知道树的深度直接按层遍历输出树的值
####有bug, 待修复
# def PrintNodeByLevel2(treeNode):
#     level = 0
#     while 1:
#         if not PrintNodeAtLevel(treeNode, level):
#             break
#         level = level + 1


PrintNodeByLevel(newTree, 5)
# PrintNodeByLevel2(newTree)

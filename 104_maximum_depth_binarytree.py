# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.max_depth = 0

    def checkDepth(self, _node, cur_depth=1):
        if _node.left:
            self.checkDepth(_node.left, cur_depth=cur_depth + 1)
        else:
            self.max_depth = max(self.max_depth, cur_depth)

        if _node.right:
            self.checkDepth(_node.right, cur_depth=cur_depth + 1)
        else:
            self.max_depth = max(self.max_depth, cur_depth)

        return self.max_depth

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        md = self.checkDepth(root)

        return md


    # def genTree(self, _vals):
    #     root = None
    #     parent = None
    #
    #     if _vals:
    #         root = TreeNode(_vals.pop(0))
    #         parent = root
    #
    #     for pos, val in enumerate(_vals):
    #         if pos % 2 == 1:
    #             parent.left = TreeNode(val)
    #         else:
    #             parent.right = TreeNode(val)


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.root = None
        self.mir_path = dict()

    def _issymm(self, node_list):
        values = list()
        childs = list()

        end_depth = True

        for node in node_list:
            if node is not None and node.val is not None:
                end_depth = False
                childs.append(node.left)
                childs.append(node.right)
                values.append(node.val)
            else:
                childs.append(None)
                childs.append(None)
                values.append(None)

        if end_depth:
            return True

        lval = len(values)
        print(values)

        for pos, val in enumerate(values[:lval // 2]):
            if val != values[lval -pos -1]:
                return False

        return self._issymm(childs)

    def _issymm2(self, node):
        if not node:
            return True

        if node not in self.mir_path:
            return False

        mir_node = self.mir_path[node]

        if not mir_node:
            return False

        if node.val != mir_node.val:
            return False

        if not node.left and mir_node.right:
            return False

        self.mir_path[node.left] = mir_node.right

        if not node.right and mir_node.left:
            return False

        self.mir_path[node.right] = mir_node.left

        l_result = self._issymm2(node.left)
        r_result = self._issymm2(node.right)

        if l_result and r_result:
            return True

        return False

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        self.root = root

        if root.left is None:
            return root.right is None

        elif root.right is None:
            return False

        if root.left.val != root.right.val:
            return False

        print("starting _issymm2")

        self.mir_path[root.left] = root.right

        return self._issymm2(root.left)

        # return self._issymm([root.left, root.right])


s = Solution()


def make_tree(node_list, values):
    child_nodes = list()

    if not values:
        return True

    if not node_list:
        return False

    for node in node_list:
        if node is None:
            continue

        val = values.pop(0)

        if not val:
            node.left = None
        else:
            node.left = TreeNode(val)

        child_nodes.append(node.left)

        if not values:
            return True

        val = values.pop(0)
        if not val:
            node.right = None
        else:
            node.right = TreeNode(val)

        child_nodes.append(node.right)

        if not values:
            return True

    return make_tree(child_nodes, values)


values = [9,14,14,74,None,None,74,None,12,12,None,63,None,None,63,-8,None,None,-8,-53,None,None,-53,None,-96,-96,None,-65,None,None,-65,98,None,None,98,50,None,None,50,None,91,91,None,41,-30,-30,41,None,86,None,-36,-36,None,86,None,-78,None,9,None,None,9,None,-78,47,None,48,-79,-79,48,None,47,-100,-86,None,47,None,67,67,None,47,None,-86,-100,-28,11,None,56,None,30,None,64,64,None,30,None,56,None,11,-28,43,54,None,-50,44,-58,63,None,None,-43,-43,None,None,63,-58,44,-50,None,54,43]
if values:
    r = TreeNode(values.pop(0))
    make_tree([r], values)

# r.left = TreeNode(2)
# r.right = TreeNode(2)
#
# r.left.left = TreeNode(3)
# r.left.right = TreeNode(1)
#
# r.right.left = TreeNode(4)
# r.right.right = TreeNode(3)

result = s.isSymmetric(r)

print(result)

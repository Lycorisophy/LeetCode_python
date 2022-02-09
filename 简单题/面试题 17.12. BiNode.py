# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Tree(object):
    def __init__(self):
        self.root = None

    def add(self, item):
        node = TreeNode(item)
        if self.root is None:
            self.root = node
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            if cur_node.left is None:
                cur_node.left = node
                return
            else:
                queue.append(cur_node.left)
            if cur_node.right is None:
                cur_node.right = node
                return
            else:
                queue.append(cur_node.right)


def convertBiNode(root: TreeNode) -> TreeNode:
    father, res = None, None

    def convert(node: TreeNode):
        if node is None:
            return
        convert(node.left)
        node.left = None
        nonlocal father, res
        if father:
            father.right = node
        else:
            res = node
        father = node
        convert(node.right)

    convert(root)
    return res


if __name__ == '__main__':
    t = Tree()
    for v in [4, 2, 5, 1, 3, None, 6, 0]:
        t.add(v)
    print(convertBiNode(t.root))

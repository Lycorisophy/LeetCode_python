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


def maxDepth(root: TreeNode) -> int:
    if not root:
        return 0
    return max(maxDepth(root.left), maxDepth(root.right)) + 1


def findMode(root: TreeNode) -> [int]:
    if not root:
        return []
    m = {}
    def preorder(node):
        if node is None:
            return
        try:
            m[node.val] += 1
        except KeyError:
            m[node.val] = 1
        preorder(node.left)
        preorder(node.right)
    preorder(root)
    res = []
    ma = max(v for k, v in m.items())
    for k, v in m.items():
        if v == ma:
            res.append(k)
    return res


if __name__ == '__main__':
    tree = Tree()
    for d in [1,None,2,2]:
        tree.add(d)
    print(findMode(tree.root))
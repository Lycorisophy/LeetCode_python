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

def isBalanced(root: TreeNode) -> bool:
    def recur(root):
        if not root:
            return 0
        left = recur(root.left)
        if left == -1:
            return -1
        right = recur(root.right)
        if right == -1:
            return -1
        return max(left, right) + 1 if abs(left - right) <= 1 else -1
    return recur(root) != -1


if __name__ == '__main__':
    t = Tree()
    for d in [1,2,2,3,3,None,None,4,4]:
        t.add(d)
    print(isBalanced(t.root))
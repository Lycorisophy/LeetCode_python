class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def add(self, x):
        node = TreeNode(x)
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

    def breadth_travel(self):
        """广度遍历"""
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.item, end=" ")
            if cur_node.lchild:
                queue.append(cur_node.left)
            if cur_node.rchild:
                queue.append(cur_node.right)

    def preorder(self, node):
        """先序遍历"""
        if node is None:
            return
        print(node.val, end=" ")
        self.preorder(node.left)
        self.preorder(node.right)

    def inorder(self, node):
        """中序遍历"""
        if node is None:
            return
        # 先处理左边的，再处理中间，然后处理后边的
        self.inorder(node.left)
        print(node.item, end=" ")
        self.inorder(node.right)

    def postorder(self, node):
        """后序遍历"""
        if node is None:
            return
        # 先处理左边的，再处理右边，然后处理中间的
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.item, end=" ")


def increasingBST(root: TreeNode) -> TreeNode:
    def _inorder(root):
        if not root:
            return []
        return _inorder(root.left) + [root.val] + _inorder(root.right)

    nodes = _inorder(root)
    n = nodes.__len__()
    root = TreeNode(nodes[0])
    head = root
    for i in range(1, n):
        root.right = TreeNode(nodes[i])
        root = root.right
    return head


if __name__ == '__main__':
    A = [5, 3, 6, 2, 4, None, 8, 1, None, None, None, 7, 9]
    t = Tree()
    for a in A:
        t.add(a)
    node = increasingBST(t.root)
    print(node)

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


def leafSimilar(root1: TreeNode, root2: TreeNode) -> bool:
    leafs1, leafs2 = [], []

    def preorder(node, leafs):
        if node is None:
            return 0
        if node.val is None:
            return 0
        if preorder(node.left, leafs) + preorder(node.right, leafs) == 0:
            leafs.append(node.val)
        return 1

    preorder(root1, leafs1)
    preorder(root2, leafs2)
    return leafs1 == leafs2


if __name__ == '__main__':
    t1, t2 = Tree(), Tree()
    root1 = [3, 5, 1, 6, 2, 9, 8, None, None, 7, 4]
    root2 = [3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8]
    for r1 in root1:
        t1.add(r1)
    for r2 in root2:
        t2.add(r2)
    print(leafSimilar(t1.root, t2.root))

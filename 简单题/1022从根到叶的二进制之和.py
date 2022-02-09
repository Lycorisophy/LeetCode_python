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
            print(cur_node.val, end=" ")
            if cur_node.left:
                queue.append(cur_node.left)
            if cur_node.right:
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
        print(node.val, end=" ")
        self.inorder(node.right)

    def postorder(self, node):
        """后序遍历"""
        if node is None:
            return
        # 先处理左边的，再处理右边，然后处理中间的
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.val, end=" ")


def sumRootToLeaf(root: TreeNode) -> int:
    arrs = []
    queue = [[root, '0b']]
    while queue:
        node, tmp = queue.pop(0)
        tmp += str(node.val)
        if node.left:
            queue.append([node.left, tmp])
        if node.right:
            queue.append([node.right, tmp])
        if not node.left and not node.right:
            arrs.append(tmp)
    return sum(int(arr, 2) for arr in arrs)


if __name__ == '__main__':
    # sum = 1
    # tmp = 1
    # res = []
    # for i in range(10):
    #     res.append(sum)
    #     tmp <<= 1
    #     sum += tmp
    # print(res)
    t1, t2, t3, t4 = Tree(), Tree(), Tree(), Tree(),
    for t in [1,1]:
        t1.add(t)
    for t in [0]:
        t2.add(t)
    for t in [1]:
        t3.add(t)
    for t in [1, 1]:
        t4.add(t)
    print(sumRootToLeaf(t1.root))
    print(sumRootToLeaf(t2.root))
    print(sumRootToLeaf(t3.root))
    print(sumRootToLeaf(t4.root))

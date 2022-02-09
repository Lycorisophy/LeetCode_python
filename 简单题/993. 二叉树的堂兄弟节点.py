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


def isCousins(root: TreeNode, x: int, y: int) -> bool:
    cnt = 0
    first_level = 0
    father_val = 0
    queue = [[root, 0, 0]]
    while queue:
        cur_node, cur_level, pre_val = queue.pop(0)
        val = cur_node.val
        if val == x or val == y:
            if cnt == 0:
                cnt += 1
                father_val = pre_val
                first_level = cur_level
            elif cnt == 1:
                if first_level == cur_level and father_val != pre_val:
                    return True
                return False
        else:
            if cur_node.left:
                queue.append([cur_node.left, cur_level + 1, val])
            if cur_node.right:
                queue.append([cur_node.right, cur_level + 1, val])
    return False


if __name__ == '__main__':
    t1 = Tree()
    t2 = Tree()
    t3 = Tree()
    for d in [1, 2, 3, 4]:
        t1.add(d)
    for d in [1, 2, 3, None, 4, None, 5]:
        t2.add(d)
    for d in [1, 2, 3, None, 4]:
        t3.add(d)
    print(isCousins(t1.root, 4, 3))
    print(isCousins(t2.root, 5, 4))
    print(isCousins(t3.root, 2, 3))

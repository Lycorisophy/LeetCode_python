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


def getMinimumDifference(root: TreeNode) -> int:
    nodes = []

    def inorder(node):
        if node is None:
            return
        inorder(node.left)
        if node.val != None:
            nodes.append(node.val)
        inorder(node.right)

    def quick_sort(nums: list, left: int, right: int) -> None:
        if left < right:
            i = left
            j = right
            # 取第一个元素为枢轴量
            pivot = nums[left]
            while i != j:
                # 交替扫描和交换
                # 从右往左找到第一个比枢轴量小的元素，交换位置
                while j > i and nums[j] > pivot:
                    j -= 1
                if j > i:
                    # 如果找到了，进行元素交换
                    nums[i] = nums[j]
                    i += 1
                # 从左往右找到第一个比枢轴量大的元素，交换位置
                while i < j and nums[i] < pivot:
                    i += 1
                if i < j:
                    nums[j] = nums[i]
                    j -= 1
            # 至此完成一趟快速排序，枢轴量的位置已经确定好了，就在i位置上（i和j)值相等
            nums[i] = pivot
            # 以i为枢轴进行子序列元素交换
            quick_sort(nums, left, i - 1)
            quick_sort(nums, i + 1, right)

    inorder(root)
    quick_sort(nodes, 0, len(nodes)-1)
    prenode = nodes[0]
    diffs = []
    for i in range(1, len(nodes)):
        diffs.append(abs(nodes[i] - prenode))
        prenode = nodes[i]
    return min(diffs)


def minDiffInBST(root: TreeNode) -> int:
    nodes = []
    def inorder(node):
        if node is None:
            return
        inorder(node.left)
        if node.val != None:
            nodes.append(node.val)
        inorder(node.right)
    inorder(root)
    prenode = nodes[0]
    diffs = []
    for i in range(1, len(nodes)):
        diffs.append(abs(nodes[i]-prenode))
        prenode = nodes[i]
    return min(diffs)


if __name__ == '__main__':
    tree = Tree()
    for d in [0,None,2236,1277,2776,519]:
        tree.add(d)
    # print(minDiffInBST(tree.root))
    print(getMinimumDifference(tree.root))

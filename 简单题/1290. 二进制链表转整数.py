class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class List:
    def __init__(self):
        self.head = None
        self.length = 0

    def isEmpty(self):
        return self.length == 0

    def append(self, dataOrNode):
        if isinstance(dataOrNode, Node):
            item = dataOrNode
        else:
            item = Node(dataOrNode)

        if not self.head:
            self.head = item
            self.length += 1

        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = item
            self.length += 1

    # 删除一个节点之后记得要把链表长度减一
    def delete(self, index):
        if self.isEmpty():
            print("this chain table is empty.")
            return

        if index < 0 or index >= self.length:
            print('error: out of index')
            return
        # 要注意删除第一个节点的情况
        # 如果有空的头节点就不用这样
        # 但是我不喜欢弄头节点
        if index == 0:
            self.head = self.head._next
            self.length -= 1
            return

        # prev为保存前导节点
        # node为保存当前节点
        # 当j与index相等时就
        # 相当于找到要删除的节点
        j = 0
        node = self.head
        prev = self.head
        while node.next and j < index:
            prev = node
            node = node.next
            j += 1

        if j == index:
            prev.next = node.next
            self.length -= 1


def getDecimalValue(head: Node) -> int:
    res = 0
    length = 29
    n = 0
    while head:
        n += 1
        res += head.val << length
        head = head.next
        length -= 1
    return res >> (30-n)


if __name__ == '__main__':
    l1 = [1, 0, 1]
    l2 = [0]
    l3 = [1]
    l4 = [1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0]
    l5 = [0, 0]
    L1 = List()
    L2 = List()
    L3 = List()
    L4 = List()
    L5 = List()
    for i1 in l1:
        L1.append(i1)
    for i2 in l2:
        L2.append(i2)
    for i3 in l3:
        L3.append(i3)
    for i4 in l4:
        L4.append(i4)
    for i5 in l5:
        L5.append(i5)
    print(getDecimalValue(L1.head))
    print(getDecimalValue(L2.head))
    print(getDecimalValue(L3.head))
    print(getDecimalValue(L4.head))
    print(getDecimalValue(L5.head))

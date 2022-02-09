class Node:

    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class MyHashSet:

    def __init__(self):
        self.data = [Node() for i in range(1000)]

    def add(self, key: int) -> None:
        p = self.data[int(str(hash(key))[-3:])]
        node = p.next
        while node:
            if node.val == key:
                break
            p = node
            node = node.next
        else:
            p.next = Node(key, None)

    def remove(self, key: int) -> None:
        p = self.data[int(str(hash(key))[-3:])]
        node = p.next
        while node:
            if node.val == key:
                p.next = node.next
                break
            p = node
            node = node.next

    def contains(self, key: int) -> bool:
        node = self.data[int(str(hash(key))[-3:])]
        while node:
            if node.val == key:
                return True
            node = node.next
        return False


if __name__ == '__main__':
    myHashSet = MyHashSet()
    myHashSet.add(1)
    myHashSet.add(2)
    myHashSet.contains(1)
    myHashSet.contains(3)
    myHashSet.add(2)
    myHashSet.contains(2)
    myHashSet.remove(2)
    myHashSet.contains(2)
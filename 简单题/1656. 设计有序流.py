class OrderedStream:

    def __init__(self, n: int):
        self.n = n
        self.values = [None]*n
        self.ptr = 1

    def insert(self, idKey: int, value: str) -> [str]:
        self.values[idKey-1] = value
        if idKey != self.ptr:
            return []
        res = [value]
        for i in range(idKey, self.n):
            tmp = self.values[i]
            if not tmp:
                self.ptr = i + 1
                return res
            res.append(tmp)
        return res


if __name__ == '__main__':
    obj = OrderedStream(5)
    print(obj.insert(3, "ccccc"))
    print(obj.insert(1, "aaaaa"))
    print(obj.insert(2, "bbbbb"))
    print(obj.insert(5, "eeeee"))
    print(obj.insert(4, "ddddd"))




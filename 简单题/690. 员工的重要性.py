class Employee:
    def __init__(self, id: int, importance: int, subordinates: [int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


def getImportance(employees: ['Employee'], id: int) -> int:
    res = 0
    emap = {e.id: [e.importance, e.subordinates] for e in employees}
    queue = [id]
    while queue:
        e = emap[queue.pop(0)]
        res += e[0]
        queue.extend(e[1])
    return res
    

if __name__ == '__main__':
    e1 = Employee(1, 5, [2, 3])
    e2 = Employee(2, 3, [])
    e3 = Employee(3, 3, [])
    print(getImportance([e1, e2, e3], 1))


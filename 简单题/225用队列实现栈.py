class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = {0: None}
        self.len = 0


    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.len += 1
        self.stack[self.len] = x


    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        tmp = self.stack[self.len]
        if self.len != 0:
            self.len -= 1
        return tmp


    def top(self) -> int:
        """
        Get the top element.
        """
        return self.stack[self.len]


    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return True if self.len == 0 else False


if __name__ == '__main__':
    # Your MyStack object will be instantiated and called as such:
    x = int(123)
    obj = MyStack()
    obj.push(x)
    param_3 = obj.top()
    param_4 = obj.empty()
    print(param_3)
    print(param_4)
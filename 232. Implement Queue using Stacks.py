class MyQueue:

    def __init__(self):
        self.stack_main = []
        self.stack_temp = []

    def push(self, x: int) -> None:
        if x:
            self.stack_main.append(x)

    def pop(self) -> int:

        for i in range(len(self.stack_main)):
            self.stack_temp.append(self.stack_main.pop())

        res = self.stack_temp.pop()
        for i in range(len(self.stack_temp)):
            self.stack_main.append(self.stack_temp.pop())

        self.stack_temp = []
        return res

    def peek(self) -> int:
        return self.stack_main[0]

    def empty(self) -> bool:
        return not bool(len(self.stack_main))


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(None)
obj.push(2)
obj.push(3)
obj.push(4)
param_2 = obj.pop()
obj.push(5)
param_5 = obj.pop()

param_3 = obj.peek()
param_4 = obj.empty()
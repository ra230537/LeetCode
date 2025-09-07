class MinStack:
    min_value = None
    def __init__(self):
        self.stack = []       

    def push(self, val: int) -> None:
        if (self.min_value == None):
            self.min_value = val
        elif (val < self.min_value):
            self.min_value = val
        self.stack.append((val, self.min_value))

    def getMin(self) -> int:
        return self.stack[-1][1]

    def pop(self) -> None:
        self.stack.pop()
        if self.stack != []:
            # Atualiza o valor minimo
            self.min_value =  self.getMin()
        else:
            self.min_value = None

    def top(self) -> int:
        return self.stack[-1][0]



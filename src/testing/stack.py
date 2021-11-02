
class Stack:
    def __init__(self):
        self.elements = []
        self.amount = 0

    def push(self, elem):
        self.elements.append(elem)
        self.amount += 1

    def pop(self):
        self.amount -= 1
        return self.elements.pop()

    def is_empty(self):
        return self.amount == 0

    def top(self):
        if self.is_empty():
            return None
        else:
            return self.elements[-1]

    def __str__(self):
        return '\n'.join(str(e) for e in self.elements)


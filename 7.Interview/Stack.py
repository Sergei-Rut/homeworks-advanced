

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


brackets = {')': '(',
            ']': '[',
            '}': '{'}


def balanced_brackets(text):
    s = Stack()
    for c in text:
        if c in brackets.values():
            s.push(c)
        elif c in brackets.keys():
            if s.isEmpty():
                return False
            elif brackets[c] != s.pop():
                return False

    return s.isEmpty()


if __name__ == '__main__':
    test_case = ('(((([{}]))))', '[([])((([[[]]])))]{()}', '{{[()]}}', '}{}', '{{[(])]}}', '[[{())}]')
    for s in test_case:
        print(balanced_brackets(list(s)))

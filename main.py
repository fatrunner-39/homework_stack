# Задание 1. Реализация класса Stack
class Stack:
    def __init__(self):
        self.elements = []

    def isEmpty(self):
        if len(self.elements) == 0:
            return True
        else:
            return False

    def push(self, el):
        self.elements.append(el)

    def pop(self):
        return self.elements.pop()

    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.elements[-1]

    def size(self):
        return len(self.elements)


# Задание 2. провеерка сбалансированности скобок.
def checkpairs(string):
    stack = Stack()
    balanced = True
    index = 0
    while index < len(string) and balanced:
        symbol = string[index]

        if symbol == '(':
            stack.push(symbol)
        elif symbol == '{':
            stack.push(symbol)
        elif symbol == '[':
            stack.push(symbol)
        elif symbol == ')':
            if stack.peek() == '(':
                stack.pop()
            else:
                balanced = False
        elif symbol == '}':
            if stack.peek() == '{':
                stack.pop()
            else:
                balanced = False
        elif symbol == ']':
            if stack.peek() == '[':
                stack.pop()
            else:
                balanced = False
        else:
            if stack.isEmpty():
                balanced = False
            else:
                stack.pop()

        index += 1

    if balanced and stack.isEmpty():
        return "Сбалансировано"
    else:
        return "Несбалансировано"


if __name__ == '__main__':
    print(checkpairs('{}'))
    print(checkpairs('(((([{()}]))))'))
    print(checkpairs('[([])((([[[]]])))]{()}'))
    print(checkpairs('[[{())}]]'))
    print(checkpairs('{[{}{}((()))]}{()()}'))
    print(checkpairs('{}'))
    print(checkpairs('({[[]]}))))'))

    stack = Stack()
    print(stack)
    stack.push(1)
    print(stack.size())
    print(stack.isEmpty())
    print(stack.peek())
    print(stack.pop())
    print(stack.isEmpty())

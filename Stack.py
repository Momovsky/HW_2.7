

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, object):
        self.items.append(object)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


def isBalanced(string):
    stack = Stack()
    flag = True
    index = 0
    while index < len(string) and flag:
        obj = string[index]
        if stack.isEmpty() and obj in ')}]':
            flag = False
        elif obj in '({[':
            stack.push(obj)
            index +=1
        else:
            obj_2 = stack.pop()
            if (obj == ')' and obj_2 == '(') or (obj == '}' and obj_2 == '{') or (obj == ']' and obj_2 == '['):
                index += 1
                continue
            else:
                flag = False
    if flag == False:
        print('Несбалансировано')
    else:
        print('Сбалансировано')




if __name__ == '__main__':
    string = input('Введите строку, состоящую из скобок: ')
    isBalanced(string)

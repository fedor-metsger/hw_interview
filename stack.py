
class Node:
    """Класс для узла стека"""
    def __init__(self, data, next_node):
        """
        Конструктор класса Node
        :param data: данные, которые будут храниться в узле
        """
        self.__data = data
        self.__next_node = next_node

    def __str__(self):
        if self.__next_node:
            return f"{self.__data}\n{self.__next_node}"
        return f"{self.__data}"

    @property
    def data(self):
        return self.__data

    @property
    def next_node(self):
        return self.__next_node

class Stack:
    """Класс для стека"""
    def __init__(self):
        """Конструктор класса Stack"""
        self.__top = None
        self.__size = 0

    def __str__(self):
        if self.__top: return str(self.__top)
        else: return ""

    def push(self, data):
        """
        Метод для добавления элемента на вершину стека
        :param data: данные, которые будут добавлены на вершину стека
        """
        node = Node(data, self.__top)
        self.__top = node
        self.__size += 1

    def pop(self):
        """
        Метод для удаления элемента с вершины стека и его возвращения
        :return: данные удаленного элемента
        """
        if not self.__top:
            return None
        node = self.__top
        self.__top = node.next_node
        self.__size -= 1
        return node.data

    def peek(self):
        """
        Метод для возврата первого элемента с вершины стека
        :return: данные удаленного элемента
        """
        if not self.__top:
            return None
        return self.__top.data

    @property
    def size(self) -> int:
        """
        Возвращает размер стека
        :return:
        """
        return self.__size

    def is_empty(self) -> bool:
        """
        Возвращает размер стека
        :return:
        """
        return self.__size == 0


def main():

    s = Stack()

    s.push(0)
    s.push(1)
    s.push(2)
    print(f'peek: {s.peek()}, size: {s.size}, is_empty: {s.is_empty()}')
    s.push("a")
    print(f'peek: {s.peek()}, size: {s.size}')
    print(f'pop: {s.pop()}')
    print(f'peek: {s.peek()}, size: {s.size}')
    print(f'peek: {s.pop()}, pop: {s.pop()}, pop: {s.pop()}, , pop: {s.pop()}, is_empty: {s.is_empty()}')


if __name__ == "__main__":
    main()
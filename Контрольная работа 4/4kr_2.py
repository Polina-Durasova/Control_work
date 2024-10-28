"""Написать программу для решения данной задачи на языке python: Создать базовый класс «список» на основе обычного массива
с функциями вставки и удаления элементов. Реализовать на базе списка производные классы стека и очереди. """


class MyList:
    def __init__(self):
        self.elements = []

    def insert(self, element):
        self.elements.append(element)

    def remove(self, element):
        if element in self.elements:
            self.elements.remove(element)
        else:
            raise ValueError("Элемент не найден в списке")

    def get_elements(self):
        return self.elements


class Stack(MyList):
    def push(self, element):
        self.insert(element)

    def pop(self):
        if not self.elements:
            raise IndexError("Стек пуст")
        return self.elements.pop()


class Queue(MyList):
    def enqueue(self, element):
        self.insert(element)

    def dequeue(self):
        if not self.elements:
            raise IndexError("Очередь пуста")
        return self.elements.pop(0)


if __name__ == "__main__":
    mylist = MyList()
    mylist.insert(1)
    mylist.insert(2)
    mylist.insert(3)
    print("Элементы стека:", mylist.get_elements())
    mylist.remove(2)
    print("Элементы стека после удаления:", mylist.get_elements())

    # Работа со стеком
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print("Элементы стека:", stack.get_elements())
    print("Удаляем элемент:", stack.pop())
    print("Элементы стека после удаления:", stack.get_elements())

    # Работа с очередью
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print("Элементы очереди:", queue.get_elements())
    print("Удаляем элемент:", queue.dequeue())
    print("Элементы очереди после удаления:", queue.get_elements())

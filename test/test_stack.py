from unittest import TestCase, main

from src.ds_stack import Stack


class TestStackMethods(TestCase):

    def test_size(self):
        stack = Stack()
        self.assertEquals(stack.size(), 0)

    def test_push(self):
        stack = Stack()
        stack.push(25)
        self.assertEquals(stack.size(), 1)

    def test_peek(self):
        stack = Stack()
        item = 32
        stack.push(item)
        self.assertEquals(stack.peek(), item)

    def test_pop(self):
        stack = Stack()
        stack.push(31)
        stack.push(64)
        stack.push(12)
        stack.push(23)
        self.assertEquals(stack.pop(), 23)

    def test_empty(self):
        stack = Stack()
        self.assertEquals(stack.empty(), True)


if __name__ == '__main__':
    main()

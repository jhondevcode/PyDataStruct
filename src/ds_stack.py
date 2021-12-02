from ds_simple_list import SimpleNode

"""
This module defines classes to simulate the operation of a stack and
perform its behaviors.

Note: the method names for the Stack class were arranged alphabetically.
"""


class Stack:
    """
    This class allows you to create and emulate the behavior of a stack in
    which the last element to enter is the first to exit. These capabilities
    are achieved thanks to the nodes which are linked through their references.
    """

    def __init__(self) -> None:
        """
        This constructor starts with the basic attributes of the stack which
        are privately encapsulated. Here the stack size is started at zero and
        the reference of the first node is also started in None which will be
        created when calling the push method.
        """
        super(Stack, self).__init__()
        self.__size = 0
        self.__top: SimpleNode = None

    def clear(self):
        """
        This method takes care of cleaning the stack by setting the reference
        of the first node to None and setting the size of the node to zero.
        """
        self.__top = None
        self.__size = 0

    def empty(self) -> bool:
        """
        It is used to be able to verify if the stack is empty.

        Returns:
            bool: True in case there are no items on the stack
        """
        return self.__size == 0 and self.__top is None

    def peek(self) -> object:
        """
        This method is used to get the last value added to the stack.

        If the stack is empty, None is returned, indicating that there are no
        values stored on the stack.

        Returns:
            object: latest added value
        """
        return self.__top.get_value() if self.__top is not None else None

    def pop(self) -> object:
        """
        Remove the last added value and return its value, since the last value
        entered will be the first value to leave the stack.

        Returns:
            object: the last element that entered the stack
        """
        if not self.empty() and self.__top is not None:
            temp_value = self.__top.get_value()
            next_node = self.__top.get_right()
            self.__top.set_value(None)
            self.__top = None
            self.__top = next_node
            self.__size -= 1
            return temp_value
        else:
            return None

    def push(self, value):
        """
        Add a value to the bottom of the stack, this mechanism is known as
        stacking.

        Internally, the value received in the parameter is inserted into a node
        to link it to the rest of the nodes through the pointer mechanism
        provided by the node.

        Args:
            value (object): The value to put at the bottom of the stack.
        """
        new_node = SimpleNode(value)
        if self.__top is None:
            self.__top = new_node
        else:
            copy = self.__top
            new_node.set_right(copy)
            self.__top = new_node
        self.__size += 1

    def size(self) -> int:
        """
        This method returns the size of the stack so far, which is the same as
        the number of stacked items it currently has.

        Returns:
            int: the number of items in the stack
        """
        return self.__size

    def __len__(self):
        """
        This method belonging to the parent class object is rewritten to be
        able to provide the output of the size of the stack using the
        function len()

        Returns:
            int: the number of items in the stack
        """
        return self.__size

    def __str__(self) -> str:
        """
        This method belonging to the parent object class is rewritten to be
        able to provide the output of the elements of the stack in the form
        of a string.

        Internally, a list is used to store the values to give the shape to
        the container of the elements.

        Returns:
            str: string representation of stack items
        """
        items = []
        temp = self.__top
        while temp is not None:
            items.append(temp.get_value())
            temp = temp.get_right()
        return str(items)

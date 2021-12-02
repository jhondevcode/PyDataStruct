from abc import ABC, abstractmethod


class GenericNode:

    def __init__(self, value):
        super(GenericNode, self).__init__()
        self.__value = value

    def delete_value(self):
        del self.__value

    def get_value(self):
        return self.__value

    def set_value(self, value):
        self.__value = value


class GenericList(ABC):

    def __init__(self):
        super(GenericList, self).__init__()
        self._size = 0

    @abstractmethod
    def add(self, value, index=None):
        pass

    @abstractmethod
    def add_all(self, collection):
        pass

    @abstractmethod
    def add_first(self, value):
        pass

    @abstractmethod
    def add_last(self, value):
        pass

    @abstractmethod
    def remove(self, value=None, index=None):
        pass

    @abstractmethod
    def remove_first(self):
        pass

    @abstractmethod
    def remove_last(self):
        pass

    @abstractmethod
    def clear(self):
        pass

    @abstractmethod
    def contains(self, value) -> bool:
        pass

    @abstractmethod
    def get(self, index: int):
        pass

    @abstractmethod
    def get_first(self):
        pass

    @abstractmethod
    def get_last(self):
        pass

    @abstractmethod
    def index_of(self, value) -> int:
        pass

    @abstractmethod
    def set(self, value, index: int):
        pass

    def empty(self) -> bool:
        return self._size == 0

    def size(self) -> int:
        return self._size

    def __len__(self) -> int:
        return self._size

    def __contains__(self, item) -> bool:
        return self.contains(item)

    def __str__(self) -> str:
        return "[]"

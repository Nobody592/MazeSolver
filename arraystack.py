"""
File: arraystack.py
Copyright 2015 by Ken Lambert

"""

from arrays import Array
from abstractstack import AbstractStack

class ArrayStack(AbstractStack):
    """An array-based stack implementation."""

    # Class variable
    DEFAULT_CAPACITY = 10

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self._items = Array(ArrayStack.DEFAULT_CAPACITY)
        AbstractStack.__init__(self, sourceCollection)

    # Accessor methods
    def __iter__(self):
        """Supports iteration over a view of self.
        Visits items from bottom to top of stack."""
        modCount = self.getModCount()
        cursor = 0
        while cursor < len(self):
            yield self._items[cursor]
            if modCount != self.getModCount():
                raise AttributeError("Illegal modification of backing store")
            cursor += 1

    def peek(self):
        """Returns the item at the top of the stack.
        Precondition: the stack is not empty.
        Raises: KeyError if stack is empty."""
        if self.isEmpty():
            raise KeyError("The stack is empty")
        return self._items[len(self) - 1]

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self._size = 0
        self._modCount = 0
        self._items = Array(ArrayStack.DEFAULT_CAPACITY)

    def push(self, item):
        """Inserts item at top of the stack."""
        # Resize array here if necessary
        if len(self) == len(self._items):
            tempArray = Array(len(self) * 2)
            for i in range(len(self)):
                tempArray[i] = self._items[i]
            self._items = tempArray
        self._items[len(self)] = item
        self._size += 1
        self.incModCount()

    def pop(self):
        """Removes and returns the item at the top of the stack.
        Precondition: the stack is not empty.
        Raises: KeyError if stack is empty.
        Postcondition: the top item is removed from the stack."""
        if self.isEmpty():
            raise KeyError("The stack is empty")
        oldItem = self._items[len(self) - 1]
        self._size -= 1
        self.incModCount()
        # Resize the array here if necessary
        if len(self) <= .25 * len(self._items) and \
           ArrayStack.DEFAULT_CAPACITY <= len(self._items) // 2:
            tempArray = Array(len(self._items) // 2)
            for i in range(len(self)):
                tempArray[i] = self._items[i]
            self._items = tempArray

        return oldItem
        
         

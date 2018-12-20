#!/usr/bin/env python3
'''
Author: dabei
My answer to Chapter 4 Quiz 2.
'''

class Array:
    '''Represents an array'''
    def __init__(self, capacity, fillValue = None):
        self._items = [fillValue for i in range(capacity)]
        # logical size
        self._logicalSize = 0

    def size(self):
        '''Get the logical size.'''
        return self._logicalSize

    def _inRange(self, index):
        '''Return if the list index is out of range'''
        if (index >= 0 and index < self.size()):
            return True
        else:
            raise IndexError('list index out of range')

    def __len__(self):
        '''Get the array length.'''
        return len(self._items)

    def __str__(self):
        return str(self._items)

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, index):
        if (self._inRange(index)):
            return self._items[index]

    def __setitem__(self, index, newItem):
        if (self._inRange(index)):
            self._items[index] = newItem

if __name__ == '__main__':
    a = Array(10)
    print(a[100])
    a[100] = 1024

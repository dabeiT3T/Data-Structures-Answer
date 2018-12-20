#!/usr/bin/env python3
'''
Author: dabei
My answer to Chapter 4 Quiz 1.
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

    def __len__(self):
        '''Get the array length.'''
        return len(self._items)

    def __str__(self):
        return str(self._items)

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, newItem):
        self._items[index] = newItem

if __name__ == '__main__':
    a = Array(10)
    print(a.size())

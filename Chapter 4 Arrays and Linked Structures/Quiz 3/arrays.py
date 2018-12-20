#!/usr/bin/env python3
'''
Author: dabei
My answer to Chapter 4 Quiz 3.
'''

class Array:
    '''Represents an array'''
    def __init__(self, capacity, fillValue = None):
        # self._items = [fillValue] * capacity
        self._items = [fillValue for i in range(capacity)]
        # logical size
        self._logicalSize = 0
        # initial capacity
        self._capacity = capacity
        # store fillValue
        self._fillValue = fillValue

    def size(self):
        '''Get the logical size.'''
        return self._logicalSize

    def _grow(self):
        '''Double array's length.'''
        if len(self) == self._logicalSize:
            items = [self._fillValue for i in range(len(self)*2)]
            for i in range(self._logicalSize):
                items[i] = self._items[i]
            self._items = items

    def _shrink(self):
        '''
        Half array's length
        when logical size is a quarter of its length,
        but not less than its initial capacity.
        '''
        if self._logicalSize < len(self)//4 and len(self) >= self._capacity*2:
            items = [self._fillValue for i in range(len(self)//2)]
            for i in range(self._logicalSize):
                items[i] = self._items[i]
            self._items = items

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
    pass
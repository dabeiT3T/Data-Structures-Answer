#!/usr/bin/env python3
'''
Author: dabei
My answer to Chapter 8 Quiz 2.
'''

class Array:
    '''Represents an array'''
    def __init__(self, capacity = 10, fillValue = None):
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

    def insert(self, pos, value):
        '''Insert value to array[pos].'''
        if pos < 0:
            raise IndexError('list index out of range')
        # if array length is not enough
        self._grow()
        pos = min(self.size(), pos)
        for i in range(self.size(), pos, -1):
            self._items[i] = self._items[i-1]
        self._items[pos] = value
         # logical size add 1
        self._logicalSize += 1

    def pop(self, pos):
        if (self._inRange(pos)):
            target = self._items[pos]
            for i in range(pos, self.size()-1):
                self._items[i] = self._items[i+1]

            self._logicalSize -= 1
            self._items[self.size()] = self._fillValue
            self._shrink()
            return target

    def remove(self, pos):
        '''Do as pop but return None.'''
        self.pop(pos)

    def _grow(self):
        '''Double array's length.'''
        if len(self) == self.size():
            items = [self._fillValue for i in range(len(self)*2)]
            for i in range(self.size()):
                items[i] = self._items[i]
            self._items = items

    def _shrink(self):
        '''
        Half array's length
        when logical size is a quarter of its length,
        but not less than its initial capacity.
        '''
        if self.size() <= len(self)//4 and len(self) >= self._capacity*2:
            items = [self._fillValue for i in range(len(self)//2)]
            for i in range(self.size()):
                items[i] = self._items[i]
            self._items = items

    def _inRange(self, index):
        '''Return if the list index is out of range'''
        # Attention: only here using len(self)!!!!!!
        if index >= 0 and index < len(self):
            return True
        else:
            raise IndexError('list index out of range')

    def __eq__(self, other):
        '''Equals.'''
        # same type
        if type(self) != type(other):
            return False
        # same length
        if self.size() != other.size():
            return False
        # same items
        for i in range(self.size()):
            if self[i] != other[i]:
                return False
        return True

    def __len__(self):
        '''Get the array length.'''
        return len(self._items)

    def __str__(self):
        return '[' + ', '.join(map(str, self._items)) + ']'

    def __iter__(self):
        # Attention: only here using iter(self._items)!!!!!!
        return iter(self._items)

    def __getitem__(self, index):
        if (self._inRange(index)):
            return self._items[index]

    def __setitem__(self, index, newItem):
        if (self._inRange(index)):
            self._items[index] = newItem

if __name__ == '__main__':
    a = Array(4)
    a.insert(0, 100)
    a.insert(0, 50)
    print(a)

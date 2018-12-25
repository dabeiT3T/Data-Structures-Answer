#!/usr/bin/env python3
'''
Author: dabei
My answer to Chapter 5 Quiz 3.
'''

from arrays import Array

class ArraySortedBag:
    '''Represents a bag :)'''
    
    DEFAULT_CAPACITY = 10

    # Constructor
    def __init__(self, sourceCollection = None):
        '''Sets the initial state of self, which includes the 
        contents of sourceCollection, if it's present.'''
        self.clear()
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)

    # Accessor methods
    def isEmpty(self):
        '''Returns True if len(self) == 0 else False.'''
        pass

    def __len__(self):
        '''Returns the number of items in self.'''
        return self._array.size()

    def __str__(self):
        '''Returns the string representation of self.'''
        return '{' + ', '.join(map(str, self)) + '}'

    def __iter__(self):
        '''Supports iteration over a view of self.'''
        return iter(self._array)

    def __add__(self, other):
        '''Returns a new bag containing the contents of self
        and other'''
        pass

    def __eq__(self, other):
        '''Return True if self equals other else False.'''
        pass

    def __contains__(self, item):
        '''Return True if item in self else False.'''
        left = 0
        right = len(self) - 1
        while left <= right:
            middle = (left + right) // 2
            if self._array[middle] == item: return True

            if self._array[middle] > item:
                right = middle - 1
            else:
                left = middle + 1
        return False

    # Mutator methods
    def clear(self):
        '''Makes self become empty.'''
        self._array = Array(ArraySortedBag.DEFAULT_CAPACITY)

    def add(self, item):
        '''Adds item to self.'''
        # avoid IndexError
        pos = 0
        for pos in range(len(self)):
            if item <= self._array[pos]:
                break
        self._array.insert(pos, item)

    def remove(self, item):
        '''Removes the item from self.'''

if __name__ == '__main__':
    asb = ArraySortedBag(list(range(9, 0, -1)))
    print(asb)          # {1, 2, 3, 4, 5, 6, 7, 8, 9}
    asb.add(0)
    print(asb)          # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
    print(11 in asb)    # False
    print(3 in asb)     # True
    for item in asb:    # 0 1 2 3 4 5 6 7 8 9 
        print(item, end=' ')
    print()

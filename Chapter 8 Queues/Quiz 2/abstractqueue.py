#!/usr/bin/env python3
'''
Author: dabei
My answer to Chapter 8 Quiz 1.
'''

class AbstractQueue:
    '''Abstact queue class with common methods.'''

    def __init__(self, items = None):
        '''Create a queue by pushing items one by one.'''
        if items is not None:
            for item in items:
                self.add(item)

    def __len__(self):
        return self._size

    def isEmpty(self):
        return len(self) == 0

    def __str__(self):
        return ' '.join(map(str, self))

    def __add__(self, other):
        '''
        Add the other queue.
        Maybe the classes had the same super class(this) can be added.
        '''
        if type(self) != type(other):
            typeSelf    = str(type(self))[1:-1].split()[1]
            typeOther   = str(type(other))[1:-1].split()[1]
            raise TypeError('unsupported operand type(s) for +: '+typeSelf+' and '+typeOther)
        # adding items one by one
        clone = type(self)(self)
        for item in other:
            clone.add(item)
        return clone

    def __eq__(self, other):
        if type(self) != type(other) or len(self) != len(other):
            return False
        if self is other:
            return True
        # u cannot use self.pop(), because it changes the queue!
        for same in map(lambda x: x[0]==x[1], zip(self, other)):
            if not same:
                return False
        return True

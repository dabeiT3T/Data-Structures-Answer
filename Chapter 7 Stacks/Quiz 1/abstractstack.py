#!/usr/bin/env python3
'''
Author: dabei
My answer to Chapter 7 Quiz 1.
'''

class AbstractStack:
    '''Abstact stack class with common methods.'''

    def __init__(self, items):
        '''Create a stack by pushing items one by one.'''
        for item in items:
            self.push(item)

    def __add__(self, other):
        '''Add the other stack.'''
        if type(self) != type(other):
            typeSelf    = str(type(self))[1:-1].split()[1]
            typeOther   = str(type(other))[1:-1].split()[1]
            raise TypeError('unsupported operand type(s) for +: '+typeSelf+' and '+typeOther)
        # pushing items one by one, form other's bottom, onto clone stack
        clone = type(self)(self)
        for item in other:
            clone.push(item)
        return clone

    def isEmpty(self):
        '''Return if the stack is empty.'''
        return False if len(self) else True;

    def __eq__(self, other):
        '''Return if 2 stacks is the same.'''
        if type(self) != type(other):
            return False
        if len(self) != len(other):
            return False
        # pop one item from each stack and check
        for same in map(lambda x: x[0]==x[1], zip(self, other)):
            if not same:
                return False
        return True

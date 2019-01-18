#!/usr/bin/env python3
'''
Author: dabei
My answer to Chapter 6 Quiz 1.
'''

import sys
from arrays import Array
from abstractstack import AbstractStack

class ArrayStack(AbstractStack): 
    '''Stack implemented by array.'''
    def __init__(self, items = []):
        self._items = Array()
        AbstractStack.__init__(self, items)

    def clear(self):
        self._items = Array()

    def pop(self):
        return self._items.pop(len(self)-1)

    def push(self, item):
        self._items.insert(len(self), item)

    def peek(self):
        return self._items[len(self)-1]

    def __len__(self):
        '''Return the size of the stack.'''
        return self._items.size()

    def __str__(self):
        '''Print from bottom to top.'''
        return ' '.join(map(str, self))

    def __iter__(self):
        '''Get item from bottom to top, but not pop them out.'''
        return iter(self._items)

if __name__ == '__main__':
    s = ArrayStack()
    print('Length: ', len(s))
    print('Empty:', s.isEmpty())
    print('Push 1-10')
    for i in range(10):
        s.push(i+1)
    print('Peeking: ', s.peek())
    print('Item (bottom to top): ', s)
    print('Length: ', len(s))
    print('Empty:', s.isEmpty())
    theClone = ArrayStack(s)
    print('Items in clone (bottom to top): ', theClone)
    theClone.clear()
    print('Length of clone after clear: ', len(theClone))
    print('Push 11')
    s.push(11)
    print('Popping items (top to bottom): ', end='')
    while not s.isEmpty():
        print(s.pop(), end=' ')
    print('\nLength: ', len(s))
    print('Empty:', s.isEmpty())
    # additional test
    print('Push 1-5')
    for i in range(5):
        s.push(i+1)
    theClone = ArrayStack(s)
    print('Equals to clone: ', s == theClone)
    print('Clone push 6')
    theClone.push(6)
    print('Equals to clone: ', s == theClone)
    print('Add clone stack: ', s + theClone)
    print('Add a number will raise an error.')
    try:
        print(s + 0)
    except TypeError as e:
        print(e, file=sys.stderr)

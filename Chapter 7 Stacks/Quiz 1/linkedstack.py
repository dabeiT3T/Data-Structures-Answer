#!/usr/bin/env python3
'''
Author: dabei
My answer to Chapter 6 Quiz 1.
'''

import sys
from links import Link
from abstractstack import AbstractStack

class LinkedStack(AbstractStack):
    '''Stack implemented by link.'''
    def __init__(self, items = None):
        self._items = Link()
        AbstractStack.__init__(self, items)

    def clear(self):
        self._items = Link()

    def pop(self):
        if self.isEmpty():
            raise KeyError('The stack is empty')
        return self._items.pop(0)

    def push(self, item):
        self._items.insert(0, item)

    def peek(self):
        if self.isEmpty():
            raise KeyError('The stack is empty')
        return self._items[0]

    def __len__(self):
        '''Return the size of the stack.'''
        return len(self._items)

    def __str__(self):
        '''Print from bottom to top.'''
        return ' '.join(map(str, self))

    def __iter__(self):
        '''Get item from bottom to top, but not pop them out.'''
        tmpList = list(self._items)
        for item in tmpList[::-1]:
            yield item

if __name__ == '__main__':
    s = LinkedStack()
    print('Length: ', len(s))
    print('Empty:', s.isEmpty())
    print('Push 1-10')
    for i in range(10):
        s.push(i+1)
    print('Peeking: ', s.peek())
    print('Item (bottom to top): ', s)
    print('Length: ', len(s))
    print('Empty:', s.isEmpty())
    theClone = LinkedStack(s)
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
    print('Pop empty stack will raise an error.')
    try:
        s.pop()
    except KeyError as e:
        print('KeyError:', e, file=sys.stderr)
    print('Push 1-5')
    for i in range(5):
        s.push(i+1)
    theClone = LinkedStack(s)
    print('Equals to clone: ', s == theClone)
    print('Clone push 6')
    theClone.push(6)
    print('Equals to clone: ', s == theClone)
    print('Add clone stack: ', s + theClone)
    print('Add a number will raise an error.')
    try:
        print(s + 0)
    except TypeError as e:
        print('TypeError:', e, file=sys.stderr)

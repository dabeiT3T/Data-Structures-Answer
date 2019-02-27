#!/usr/bin/env python3
'''
Author: dabei
My answer to Chapter 8 Quiz 1.
'''

import sys
from nodes import Node
from abstractqueue import AbstractQueue

class LinkedQueue(AbstractQueue):
    '''Represents a linked queue'''

    def __init__(self, items = None):
        self.clear()
        AbstractQueue.__init__(self, items)

    def clear(self):
        self._head = None
        self._rear = self._head
        self._size = 0

    def peek(self):
        '''Return the item at the queue's front.'''
        if self.isEmpty():
            raise KeyError('The queue is empty')
        return self._head.data

    def add(self, item):
        '''Add the item to the queue's rear.'''
        newNode = Node(item, None)
        if self.isEmpty():
            self._head = newNode
        else:
            self._rear.next = newNode
        self._rear = newNode
        self._size += 1

    def pop(self):
        '''Pop the item at the queue's front.'''
        if self.isEmpty():
            raise KeyError('The queue is empty')
        item = self._head.data
        self._head = self._head.next
        if self._head is None:
            self._rear = self._head
        self._size -= 1
        return item

    def __iter__(self):
        probe = self._head
        for i in range(len(self)):
            yield probe.data
            probe = probe.next


if __name__ == '__main__':
    queue = LinkedQueue()
    print('Length:', len(queue))
    print('Empty:', queue.isEmpty())
    print('Add a, b, c')
    queue.add('a')
    queue.add('b')
    queue.add('c')
    print('Queue:', *queue)
    print('Length:', len(queue))
    print('Empty:', queue.isEmpty())
    print('Peek:', queue.peek())
    print('Pop:', queue.pop())
    print('Pop:', queue.pop())
    print('Pop:', queue.pop())
    print('Empty:', queue.isEmpty())
    print('Call peek() will raise an error.')
    try:
        queue.peek()
    except KeyError as e:
        print('KeyError:', e, file=sys.stderr)

    print('Call pop() will raise an error.')
    try:
        queue.pop()
    except KeyError as e:
        print('KeyError:', e, file=sys.stderr)
    print('Add d')
    queue.add('d')
    newQueue = LinkedQueue(range(5))
    print('New queue:', newQueue)
    print('Add to the new queue:', queue+newQueue)
    print('Add a number will raise an error.')
    try:
        sum = queue + 4
    except TypeError as e:
        print('TypeError:', e, file=sys.stderr)

#!/usr/bin/env python3
'''
Author: dabei
My answer to Chapter 8 Quiz 3.
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

    def _inRange(self, index):
        '''Return if the queue index is out of range'''
        if index >= 0 and index < len(self):
            return True
        else:
            raise IndexError('queue index out of range')

    def remove(self, index):
        '''Return the item at index and remove it.'''
        if self._inRange(index):
            # no head node :(
            if index == 0:
                item = self._head.data
                self._head = self._head.next
            else:
                probe = self._head
                for i in range(index-1):
                    probe = probe.next
                item = probe.next.data
                probe.next = probe.next.next
            self._size -= 1
            # reset the rear
            probe = self._head
            for i in range(len(self)-1):
                probe = probe.next
            self._rear = probe
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
    print('Add a, b, c, z')
    queue.add('a')
    queue.add('b')
    queue.add('c')
    queue.add('z')
    print('Queue:', queue)
    print('Remove 3:', queue.remove(3))
    print('Queue:', queue)
    print('Add d')
    queue.add('d')
    print('Queue:', queue)
    print('Remove 0:', queue.remove(0))
    print('Queue:', queue)
    print('Remove 0:', queue.remove(0))

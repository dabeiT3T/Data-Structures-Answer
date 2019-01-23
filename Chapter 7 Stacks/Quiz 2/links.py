#!/usr/bin/env python3
'''
Author: dabei
My answer to Chapter 4 Quiz 10.
'''

from nodes import Node

class Link:
    '''Represents a link'''
    def __init__(self, items = None):
        # Create a link list with None head
        self._head = Node(None, None)
        self._head.next = self._head
        self._logicalSize = 0
        if items is not None:
            self.createList(items)


    def createList(self, iterator) -> None:
        '''
        Create a link list with None head and keep the order.
        '''
        probe = self._head
        for data in iterator:
            self._logicalSize += 1
            probe.next = Node(data, self._head)
            probe = probe.next

    def insert(self, pos, data) -> None:
        '''Insert data into list.'''
        if pos < 0:
            raise IndexError('list index out of range')

        probe = self._head
        while pos > 0 and probe.next != self._head:
            pos -= 1
            probe = probe.next

        probe.next = Node(data, probe.next)
        self._logicalSize += 1

    def pop(self, pos):
        if self._inRange(pos):
            probe = self._head
            while pos > 0 and probe.next.next != self._head:
                pos -= 1
                probe = probe.next

            data = probe.next.data
            probe.next = probe.next.next
            self._logicalSize -= 1
            return data

    def _inRange(self, index):
        '''Return if the list index is out of range'''
        if index >= 0 and index < len(self):
            return True
        else:
            raise IndexError('list index out of range')

    def __len__(self):
        return self._logicalSize

    def __iter__(self):
        probe = self._head.next
        while probe != self._head:
            yield probe.data
            probe = probe.next

    def __str__(self):
        return ' '.join(map(str, self))

    def __getitem__(self, index):
        if (self._inRange(index)):
            probe = self._head.next
            for pos in range(index, 0, -1):
                probe = probe.next
            return probe.data

if __name__ == '__main__':
    link = Link(range(10))
    print('create link:', *link)
    print('link size:', len(link))
    print('link pop 4:', link.pop(4))
    print('link has:', link)
    print('link size:', len(link))
    print('insert 100 at 5.')
    link.insert(5, 100)
    print('link has:', link)
    print('index 5:', link[5])
    print('index 9:', link[9])

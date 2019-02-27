#!/usr/bin/env python3
'''
Author: dabei
My answer to Chapter 8 Quiz 2.
'''

import sys
from arrays import Array
from abstractqueue import AbstractQueue

class ArrayQueue(AbstractQueue):
    '''Represents a linked queue'''

    # default array's capacity
    CAPACITY = 10

    def __init__(self, items = None):
        self.clear()
        AbstractQueue.__init__(self, items)

    def clear(self):
        self._array = Array(ArrayQueue.CAPACITY)
        self._head = 0
        self._rear = self._head
        self._size = 0

    def peek(self):
        '''Return the item at the queue's front.'''
        if self.isEmpty():
            raise KeyError('The queue is empty')
        return self._array[self._head]

    def add(self, item):
        '''Add the item to the queue's rear.'''
        # increase the _array
        self._grow()
        if self.isEmpty():
            # _head == _rear
            self._array[self._rear] = item
        else:
            # _rear += 1 and _array[_rear] = item
            # when _rear + 1 >= len(_array), 
            # move the rear to the head of _array
            self._rear = (self._rear+1) % len(self._array)
            self._array[self._rear] = item
        self._size += 1

    def pop(self):
        '''Pop the item at the queue's front.'''
        if self.isEmpty():
            raise KeyError('The queue is empty')
        # get the head item
        item = self._array[self._head]
        if self._head != self._rear:
            # _head runs towards _rear
            self._head = (self._head+1) % len(self._array)
        self._size -= 1
        # decrease the _array
        self._shrink()
        return item

    def _copyToNewArray(self, newArray):
        for index, item in enumerate(self):
                newArray[index] = item
        # reset _head & _rear
        self._head = 0
        self._rear = len(self) - 1
        self._array = newArray

    def _grow(self):
        '''Double array's length.'''
        if len(self) == len(self._array):
            # create a double array
            newArray = Array(len(self._array)*2)
            # copy
            self._copyToNewArray(newArray)

    def _shrink(self):
        '''
        Half array's length
        when logical size is a quarter of its length,
        but not less than its initial capacity.
        '''
        if len(self) <= len(self._array)//4 and len(self._array) >= ArrayQueue.CAPACITY*2:
            # create a half-size array
            newArray = Array(len(self._array)//2)
            self._copyToNewArray(newArray)


    def __iter__(self):
        for i in range(len(self)):
            index = (self._head + i) % len(self._array)
            yield self._array[index]


if __name__ == '__main__':
    queue = ArrayQueue()
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
    newQueue = ArrayQueue(range(5))
    print('New queue:', newQueue)
    print('Add to the new queue:', queue+newQueue)
    print('Add a number will raise an error.')
    try:
        sum = queue + 4
    except TypeError as e:
        print('TypeError:', e, file=sys.stderr)

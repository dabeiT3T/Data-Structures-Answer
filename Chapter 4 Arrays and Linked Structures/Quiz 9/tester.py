#!/usr/bin/env python3
'''
Author: dabei
My answer to Chapter 4 Quiz 9.
'''

from nodes import Node

def createList(iterator) -> Node:
    '''
    Create a link list with None head and keep the order.
    '''
    head = Node(None, None)
    head.next = head
    probe = head
    for data in iterator:
        probe.next = Node(data, head)
        probe = probe.next
    # node head
    return head

def length(head):
    '''Count the link list with None head.'''
    probe = head.next
    count = 0
    while probe != head:
        count += 1
        probe = probe.next
    return count

def iterList(head):
    probe = head.next
    while probe != head:
        yield probe.data
        probe = probe.next

def insert(data, pos, head):
    '''Insert data into list.'''
    if pos < 0:
        raise IndexError('list index out of range')

    probe = head
    while pos > 0 and probe.next != head:
        pos -= 1
        probe = probe.next

    probe.next = Node(data, probe.next)
    return head


if __name__ == '__main__':
    head = createList(range(10))
    print(*iterList(head))
    head = insert(100, 4, head)
    print(*iterList(head))

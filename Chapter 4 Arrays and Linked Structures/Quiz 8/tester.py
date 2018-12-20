#!/usr/bin/env python3
'''
Author: dabei
My answer to Chapter 4 Quiz 8.
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
        probe.next = Node(data, None)
        probe = probe.next
    # node head
    return head

def length(head):
    '''Count the link list with None head.'''
    probe = head.next
    count = 0
    while probe.next:
        count += 1
        probe = probe.next
    return count

if __name__ == '__main__':
    head = createList(range(10))
    print(length(head))

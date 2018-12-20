#!/usr/bin/env python3
'''
Author: dabei
My answer to Chapter 4 Quiz 11.
'''

from nodes import Node, TwoWayNode

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

def iterList(head):
    probe = head.next
    while probe != head:
        yield probe.data
        probe = probe.next

def makeTwoWay(head):
    '''Make one way into two way list with None head.'''
    thead = TwoWayNode(None, None, None)
    thead.provious = thead.next = thead
    tail = thead
    probe = thead
    for data in iterList(head):
        probe.next = TwoWayNode(data, probe, thead)
        probe = probe.next
        tail = probe
    return thead, tail

if __name__ == '__main__':
    head = createList(range(10))
    print(*iterList(head))
    # make one way into two way
    thead, tail = makeTwoWay(head)
    print(*iterList(thead))
    probe = tail
    while probe != thead:
        print(probe.data, end = ' ')
        probe = probe.provious
    print()

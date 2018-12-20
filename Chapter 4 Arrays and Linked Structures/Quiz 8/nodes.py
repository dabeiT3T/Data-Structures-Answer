#!/usr/bin/env python3
'''
Author: dabei
A singly linked node
'''

class Node:
    '''Represents a singly linked node.'''

    def __init__(self, data, next = None):
        self.data = data
        self.next = next
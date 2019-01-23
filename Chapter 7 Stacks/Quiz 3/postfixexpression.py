#!/usr/bin/env python3
'''
Author: dabei
My answer to Chapter 7 Quiz 3.
'''

from linkedstack import LinkedStack

class PostfixExpression:
    '''Operate the postfix expression.'''

    _operator = {
        '+': (lambda x, y: x + y),
        '-': (lambda x, y: x - y),
        '*': (lambda x, y: x * y),
        '/': (lambda x, y: x / y),
    }

    def __init__(self, expression):
        self._expression = expression
        self._tokens = self._expression.split()

    def operate(self):
        '''Operate the postfix expression.'''
        stack = LinkedStack()
        for operand in self._tokens:
            if operand not in PostfixExpression._operator:
                # push the operand to the stack
                stack.push(operand)
            else:
                # operate two operand on the top of stack with the operation
                opRight = float(stack.pop())
                opLeft = float(stack.pop())
                res = PostfixExpression._operator[operand](opLeft, opRight)
                # push the result onto the stack
                stack.push(res)
        return stack.pop()

    def __str__(self):
        return self._expression

if __name__ == '__main__':
    exp = '20 30 40 + 10 - -'
    pe = PostfixExpression(exp)
    print(pe, '=', pe.operate())

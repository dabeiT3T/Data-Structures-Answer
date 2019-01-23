#!/usr/bin/env python3
'''
Author: dabei
My answer to Chapter 7 Quiz 6.
'''

class Token:
    '''Convert infix expression to postfix expression.'''

    UNKOWN = 0      # unkown

    FLOAT = 3       # float
    INT = 4         # integer

    MINUS = 5       # minus   operator
    PLUS = 6        # plus    operator
    MUL = 7         # muliply operator
    DIV = 8         # divide  operator

    POW = 10        # pow     operator

    OPENPAREN = 20  # open paren
    CLOSEPAREN = 21 # close paren

    FIRST_OP = 5    # first operator code

    operator = {
        '+': (lambda x, y: x + y),
        '-': (lambda x, y: x - y),
        '*': (lambda x, y: x * y),
        '/': (lambda x, y: x / y),
        '^': (lambda x, y: x ** y),
        '(': None,
        ')': None,
    }

    _opType = {
        '+': PLUS,
        '-': MINUS,
        '*': MUL,
        '/': DIV,
        '^': POW,
        '(': OPENPAREN,
        ')': CLOSEPAREN,
    }

    _opLevel = {
        MINUS: 10,
        PLUS: 10,
        MUL: 20,
        DIV: 20,
        POW: 30,
        OPENPAREN: 100,
        CLOSEPAREN: 100,
    }

    def __init__(self, value):
        if type(value) == float:
            self._type = Token.FLOAT
        else:
            self._type = self._makeType(value)
        self._precedence = self._makePrecedence()
        self._value = value

    def isOperator(self):
        return self._type >= Token.FIRST_OP

    def __str__(self):
        return str(self._value)

    def getType(self):
        return self._type

    def getValue(self):
        return self._value

    def getPrecedence(self):
        return self._precedence

    def _makeType(self, ch):
        if ch in Token._opType:
            return Token._opType[ch]
        else:
            return Token.UNKOWN

    def _makePrecedence(self):
        if self._type in Token._opLevel:
            return Token._opLevel[self._type]
        else:
            return 0

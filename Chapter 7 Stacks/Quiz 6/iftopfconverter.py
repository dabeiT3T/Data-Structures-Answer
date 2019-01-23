#!/usr/bin/env python3
'''
Author: dabei
My answer to Chapter 7 Quiz 5.
'''

from token import Token
from scanner import Scanner
from linkedstack import LinkedStack

class IFToPFConverter:
    '''Convert infix expression to postfix expression.'''

    def __init__(self, scanner):
        # if type(scanner) == Scanner
        self._scanner = scanner
        self._pfTokens = None

    def convert(self):
        # cache the result
        if not self._pfTokens:
            # save the converted expression (tokens)
            self._pfTokens = []
            # stack to store operators and operands
            stack = LinkedStack()
            for token in self._scanner:
                # append the operand to list
                if not token.isOperator():
                    self._pfTokens.append(token)
                # Token.OPENPAREN & Token.CLOSEPAREN are operators,
                # so must be called before token.isOperator().
                elif token.getType() == Token.OPENPAREN:
                    stack.push(token)
                elif token.getType() == Token.CLOSEPAREN:
                    for i in range(len(stack)):
                        operator = stack.pop()
                        if operator.getType() == Token.OPENPAREN:
                            break
                        self._pfTokens.append(operator)
                elif token.isOperator():
                    # pop operators in the stack whose precedence is not smaller
                    for i in range(len(stack)):
                        if (stack.peek().getType() == Token.OPENPAREN or
                            stack.peek().getPrecedence() < token.getPrecedence() or (
                            stack.peek().getType() == Token.POW and 
                            token.getType() == Token.POW)):
                            break
                        self._pfTokens.append(stack.pop())
                    stack.push(token)

            for i in range(len(stack)):
                self._pfTokens.append(stack.pop())

        return self._pfTokens

    def __inter__(self):
        if not self._pfTokens:
            self.convert()
        return iter(self._pfTokens)

    def __str__(self):
        if not self._pfTokens:
            self.convert()
        return ' '.join(map(str, self._pfTokens))

if __name__ == '__main__':
    ife = '2^2^3'
    scanner = Scanner(ife)
    print('Infix expression:', scanner)
    converter = IFToPFConverter(scanner)
    tokenList = converter.convert()
    print(*tokenList)
    print(converter)

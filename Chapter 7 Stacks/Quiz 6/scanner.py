#!/usr/bin/env python3
'''
Author: dabei
My answer to Chapter 7 Quiz 5.
'''

from token import Token

class Scanner:
    '''Scanner a string and split it.'''

    def __init__(self, sourceStr):
        self._sourceStr = sourceStr
        # do scanning
        self._scan()

    def _scan(self) -> None:
        '''Scan a expression and find out operands and operators even without blanks'''
        self.tokens = []
        # index of a number starting at
        tokenStart = 0
        # delete blanks
        withoutBlank = self._sourceStr.replace(' ', '')
        # read the expression
        for index, char in enumerate(withoutBlank):
            # meeting an operator means the end of a number
            if char in Token.operator:
                # skip '()'
                if index != tokenStart:
                    # append the operand
                    self.tokens.append(Token(float(withoutBlank[tokenStart:index])))
                # append the operator or '()'
                self.tokens.append(Token(char))
                # update the numberStart's index
                tokenStart = index + 1
            # append the last number
            elif index == len(withoutBlank) - 1:
                self.tokens.append(Token(float(withoutBlank[tokenStart:index+1])))

    def __iter__(self):
        return iter(self.tokens)

    def __str__(self):
        return ' '.join(map(str, self))

if __name__ == '__main__':
    expression = '12.12 +(4/3.14 - 10)*2'
    s = Scanner(expression)
    print('Scann:', expression)
    print(*(token.getValue() for token in s.tokens))
    print(*(token.getType() for token in s.tokens))

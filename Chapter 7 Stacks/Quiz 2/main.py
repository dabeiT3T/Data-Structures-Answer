#!/usr/bin/env python3
'''
Author: dabei
My answer to Chapter 7 Quiz 1.
'''

from linkedstack import LinkedStack

def isPalindrome(word: str) -> bool:
    '''
    True if a word read from left equal to from right else False.
    '''
    wordLen = len(word)
    if wordLen == 1 or wordLen == 0:
        return True

    stack = LinkedStack()
    middle = wordLen // 2
    for index in range(0, middle):
        stack.push(word[index])

    for index in range(wordLen-middle, wordLen):
        if word[index] != stack.pop():
            return False
    return True

if __name__ == '__main__':
    print('noon is palidrome:', isPalindrome('noon'))
    print('ewe is palidrome:', isPalindrome('ewe'))
    print('reviver is palidrome:', isPalindrome('reviver'))
    print('peek is palidrome:', isPalindrome('peek'))

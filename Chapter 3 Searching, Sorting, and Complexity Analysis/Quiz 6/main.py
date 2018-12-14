#!/usr/bin/env python3
'''
Author: dabei
My answer to Chapter 3 Quiz 6.

complexity: O(2(n-2)+1) = O(2n-3) ≈ O(n)
'''

class Counter:
    def __init__(self):
        self._counter = 0

    def increment(self):
        self._counter += 1

    def __str__(self):
        return str(self._counter)

def fib(n: int, d: dict, counter: Counter) -> int:
    counter.increment()
    if n < 3: return 1

    if not n in d:
        d[n] = fib(n - 1, d, counter) + fib(n - 2, d, counter)

    return d[n]

def main() -> None:
    d = {}
    counter = Counter()
    print(fib(6, d, counter))
    print(counter)

# test
if __name__ == '__main__':
    main()

#!/usr/bin/env python3
'''
Author: dabei
My answer to Chapter 3 Quiz 9.
'''

import time
from random import randint

class Profiler:
    def __init__(self, lyst: list, sublen: int = 50):
        self._length = len(lyst)
        self._sublen = sublen
        # exchange count
        self._exchCount = 0
        # comarison count
        self._cmpCount = 0
        self._mixedSort = MixedSort(lyst, sublen, self)
        self._startClock()
        self._mixedSort.quicksort()
        self._stopClock()

    def _startClock(self):
        self._start = time.time()

    def _stopClock(self):
        self._elapsedTime = round(time.time() - self._start, 3)

    def exchange(self):
        self._exchCount += 1

    def comparison(self):
        self._cmpCount += 1

    def getMixedSort(self):
        return self._mixedSort

    def __str__(self):
        result = 'Problem size: '
        result += str(self._length) + '\n'
        result += 'Insertsort list length: '
        result += str(self._sublen) + '\n'
        result += 'Elapsed time: '
        result += str(self._elapsedTime) + '\n'
        result += 'Comparisons: '
        result += str(self._cmpCount) + '\n'
        result += 'Exhcange: '
        result += str(self._exchCount)
        return result

class MixedSort:
    def __init__(self, lyst: list, sublen: int, profiler: Profiler):
        self._lyst = lyst
        self._sublen = sublen
        self._profiler = profiler

    def swap(self, left: int, right: int) -> None:
        self._profiler.exchange()
        self._lyst[left], self._lyst[right] = self._lyst[right], self._lyst[left]

    def insertsort(self, head: int, tail: int) -> None:
        for i in range(head+1, tail+1):
            move = i
            for j in range(i-1, head-1, -1):
                self._profiler.comparison()
                if self._lyst[move] < self._lyst[j]:
                    self.swap(move, j)
                    move = j
                else:
                    break

    def quicksort(self) -> None:
        self.quicksortHelper(0, len(self._lyst)-1)

    def quicksortHelper(self, head: int, tail: int) -> None:
        # Contidition comparison does not include in _profiler._cmpCount.
        if head < tail:
            if tail - head + 1 > self._sublen:
                pivot = self.partition(head, tail)
                # left part
                self.quicksortHelper(head, pivot-1)
                # right part
                self.quicksortHelper(pivot+1, tail)
            else:
                # when len(partition) is short
                # use insertsort instead
                self.insertsort(head, tail)

    def partition(self, head: int, tail: int) -> int:
        middle = (head + tail) // 2
        self.swap(middle, tail)

        pivot = head
        for i in range(head, tail):
            self._profiler.comparison()
            if self._lyst[i] < self._lyst[tail]:
                self.swap(pivot, i)
                pivot += 1

        self.swap(pivot, tail)
        return pivot

    def __str__(self):
        return str(self._lyst)

def main() -> None:
    size = 5000
    L = [randint(0, size) for i in range(size)]
    # print(L)
    profiler = Profiler(L, 20)
    print(profiler)
    # print(profiler.getMixedSort())

# test
if __name__ == '__main__':
    main()

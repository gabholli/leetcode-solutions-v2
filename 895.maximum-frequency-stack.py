#
# @lc app=leetcode id=895 lang=python
#
# [895] Maximum Frequency Stack
#

# @lc code=start

from heapq import *


class Element:

    def __init__(self, string, freq, seq_num):
        self.string = string
        self.freq = freq
        self.seq_num = seq_num

    def __lt__(self, other):
        if self.freq != other.freq:
            return self.freq > other.freq
        return self.seq_num > other.seq_num


class FreqStack(object):

    def __init__(self):
        self.max_heap = []
        self.freq = {}
        self.seq_num = 0

    def push(self, val):
        self.freq[val] = self.freq.get(val, 0) + 1
        heappush(self.max_heap, Element(
            val, self.freq[val], self.seq_num
        ))
        self.seq_num += 1

    def pop(self):
        word = heappop(self.max_heap).string

        if self.freq[word] > 0:
            self.freq[word] -= 1
        else:
            del self.freq[word]

        return word

    # O(nlog(n)) T, O(n) S

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
# @lc code=end

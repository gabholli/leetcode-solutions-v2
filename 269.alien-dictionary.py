#
# @lc app=leetcode id=269 lang=python
#
# [269] Alien Dictionary
#

# @lc code=start
from collections import deque


class Solution(object):
    def alienOrder(self, words):
        sorted_order = []

        if len(words) == 0:
            return ''

        graph, in_degree = {}, {}

        for word in words:
            for char in word:
                graph[char] = []
                in_degree[char] = 0

        for i in range(0, len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            for j in range(0, max(len(w1), len(w2))):
                if j == len(w1):
                    break
                if j == len(w2):
                    return ''

                parent, child = w1[j], w2[j]
                if parent != child:
                    graph[parent].append(child)
                    in_degree[child] += 1
                    break

        sources = deque()

        for key in in_degree:
            if in_degree[key] == 0:
                sources.append(key)

        while sources:
            vertex = sources.popleft()
            sorted_order.append(vertex)
            for child in graph[vertex]:
                in_degree[child] -= 1
                if in_degree[child] == 0:
                    sources.append(child)

        if len(sorted_order) != len(in_degree):
            return ''

        return ''.join(sorted_order)

    # O(v + n) T , O(v + n) S

# @lc code=end

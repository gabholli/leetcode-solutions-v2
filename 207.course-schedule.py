#
# @lc app=leetcode id=207 lang=python
#
# [207] Course Schedule
#

# @lc code=start
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        sorted_order = []

        if numCourses <= 0:
            return []

        in_degree = {i: 0 for i in range(numCourses)}
        graph = {i: [] for i in range(numCourses)}

        for pre in prerequisites:
            parent, child = pre[0], pre[1]
            graph[parent].append(child)
            in_degree[child] += 1

        sources = []

        for key in in_degree:
            if in_degree[key] == 0:
                sources.append(key)

        while sources:
            vertex = sources.pop(0)
            sorted_order.append(vertex)
            for child in graph[vertex]:
                in_degree[child] -= 1
                if in_degree[child] == 0:
                    sources.append(child)

        return len(sorted_order) == numCourses

    # O(v + e) T, O(v + e) S
# @lc code=end

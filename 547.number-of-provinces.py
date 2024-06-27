#
# @lc app=leetcode id=547 lang=python
#
# [547] Number of Provinces
#

# @lc code=start
class Solution(object):
    def findCircleNum(self, isConnected):
        provinces = 0

        def dfs(city):
            for i in range(len(isConnected)):
                if isConnected[city][i] == 1 and not visited[i]:
                    visited[i] = True
                    dfs(i)

        visited = [False] * len(isConnected)

        for city in range(len(isConnected)):
            if not visited[city]:
                dfs(city)
                provinces += 1

        return provinces

    # O(n^2) T, O(n) S

# @lc code=end

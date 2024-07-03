#
# @lc app=leetcode id=1539 lang=python
#
# [1539] Kth Missing Positive Number
#

# @lc code=start
class Solution(object):
    def findKthPositive(self, arr, k):
        missing = []
        i = 0
        n = len(arr)

        while i < n:
            j = arr[i] - 1
            if arr[i] > 0 and arr[i] <= n and arr[i] != arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
            else:
                i += 1

        extra_numbers = set()

        for i in range(n):
            if arr[i] != i + 1:
                if len(missing) < k:
                    extra_numbers.add(arr[i])
                    missing.append(i + 1)

        i = 1

        while len(missing) < k:
            candidate = i + n
            if candidate not in extra_numbers:
                missing.append(candidate)
            i += 1

        return missing[-1]

    # O(n + k) T, O(k) S

# @lc code=end

#
# @lc app=leetcode id=1720 lang=python
#
# [1720] Decode XORed Array
#

# @lc code=start
class Solution(object):
    def decode(self, encoded, first):
        answer = []
        answer.append(first)

        for i in range(1, len(encoded) - 1):
            answer.append(encoded[i] ^ encoded[i + 1])

        return answer

    # O(n) T, O(n) S

# @lc code=end

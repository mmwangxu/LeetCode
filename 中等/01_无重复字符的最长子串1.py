"""
给定一个字符串，请你找出其中不含有重复字符的最长子串的长度。

示例1:
输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是"wke"，所以其长度为 3。
请注意，你的答案必须是子串的长度，"pwke"是一个子序列，不是子串。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
"""

class Solution:
    def lengthOfLongestSubstring(self, s):
        count = 0
        list_str = s
        # list_str = [str(i) for i in s]
        length = len(list_str)
        list_norep = []
        len_list = []
        for j in range(0, length):
            for i in range(j, length):
                if list_str[i] not in list_norep:
                    list_norep.append(list_str[i])
                    count += 1
                    len_list.append(len(list_norep))
                    if i == length-1:
                        list_norep = []
                        count = 0
                else:
                    list_norep = []
                    count = 0
                    break

        if sum(len_list) == 0 and len(list_norep) == 0:
            return 0
        else:
            return max(len_list)


solution = Solution()
l = solution.lengthOfLongestSubstring(s='pwwkew')
print(l)

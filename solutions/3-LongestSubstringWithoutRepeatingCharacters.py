# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# time out
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maximum = 0
        for i in range(len(s)):
            dic = {}
            start = i
            for index, c in enumerate(s[i:]):
                if c in dic:
                    maximum = maximum if len(dic.keys()) < maximum else len(dic.keys())
                    start = index
                    dic = {c: 1}
                else:
                    dic[c] = 1
            
            maximum = maximum if len(dic.keys()) < maximum else len(dic.keys())
        
        return maximum

print(Solution().lengthOfLongestSubstring('b' * 5000))
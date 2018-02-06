class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        for i, chars in enumerate(zip(*strs)):
            if len(set(chars)) > 1:
                return strs[0][:i]
            
        return min(strs)

s = Solution()

r = s.longestCommonPrefix(["aa", "acaa", 'dd'])

print("result: %s" % r)

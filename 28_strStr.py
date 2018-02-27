class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not haystack:
            if not needle:
                return 0
            
            return -1

        for pos, c in enumerate(haystack):
            if haystack[pos:].startswith(needle):
                return pos

        return -1
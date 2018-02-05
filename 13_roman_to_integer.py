class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        prev = None

        rule = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        for c in s:
            num_c = rule[c]
            result += num_c

            if prev is not None and num_c > prev:
                result -= prev * 2

            prev = num_c

        return result

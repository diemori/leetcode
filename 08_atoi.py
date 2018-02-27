class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        sign = 1
        base = 0
        i = 0

        if not str:
            return 0

        while str[i] == ' ':
            i += 1

        if str[i] == '-' or str[i] == '+':
            sign = 1 - 2 * (str[i] == '-')
            i += 1

        for c in str[i:]:
            if not c.isdigit():
                break

            base = 10 * base + int(c)

        if sign == 1:
            return min(base, 2147483647)
        else:
            return max(-1 * base, -2147483648)


s = Solution()

r = s.myAtoi("-4")

print(r)

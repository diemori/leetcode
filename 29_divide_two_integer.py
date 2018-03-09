class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        summed = 0
        result = 0

        pos = (1 - 2 * (dividend < 0))
        pos = pos * (1 - 2 * (divisor < 0))

        abs_d = abs(dividend)
        abs_r = abs(divisor)

        if abs_r > abs_d:
            return 0

        if abs_r == 1:
            return min(max(abs_d * pos, -2147483648), 2147483647)

        while summed < abs_d:
            summed += abs_r
            result += 1

        if summed > abs_d:
            result -= 1

        return min(max(result * pos, -2147483648), 2147483647)


s = Solution()

r = s.divide(1, 1)

print(r)

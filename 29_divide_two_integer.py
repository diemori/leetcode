class Solution:
    def __init__(self):
        self.int_max = 2147483647
        self.int_min = -2147483648

    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        result = 0
        current_bit = 1

        p = 1

        if dividend < 0:
            p = ~p
            dividend = ~dividend + 1

        if divisor < 0:
            p = ~p
            divisor = ~divisor + 1

        d = divisor

        while d <= dividend:
            d = d << 1
            current_bit = current_bit << 1

        while d >= divisor:
            d = d >> 1
            current_bit = current_bit >> 1

            if d <= dividend:
                dividend -= d
                result += current_bit

        if p < 0:
            result = ~result + 1

        return min(max(result, self.int_min), self.int_max)


s = Solution()

r = s.divide(10, -3)

print(r)

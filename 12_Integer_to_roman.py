class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        rule = {
            1000: 'M',
            500: 'D',
            100: 'C',
            50: 'L',
            10: 'X',
            5: 'V',
            1: 'I'
        }

        # rule_pattern = [1000, 500, 100, 50, 10, 5, 1]

        rest = num
        div = 1000

        result = ""

        while div >= 1:
            div = int(div)

            if div > rest:
                div /= 10
                continue

            dresult, rest = rest // div, rest % div

            if dresult == 9:
                result += rule[div] + rule[div*10]
            elif dresult > 4:
                result += rule[div * 5] + (rule[div] * (dresult - 5))
            elif dresult == 4:
                result += rule[div] + rule[div*5]
            else:
                result += rule[div] * dresult

            div /= 10

        return result


s = Solution()

r = s.intToRoman(9)

print(r)

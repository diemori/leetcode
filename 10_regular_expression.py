class Solution(object):
    def isMatch(self, text, pattern):
        memo = {}

        def dp(i, j):
            if (i, j) in memo:
                return memo[i, j]

            if j == len(pattern):
                ans = i == len(text)
            else:
                first_match = i < len(text) and pattern[j] in {text[i], '.'}

                if j+1 < len(pattern) and pattern[j+1] == '*':
                    # try both (ignoring *) and (using *)
                    ans = dp(i, j+2) or first_match and dp(i+1, j)
                else:
                    # go to next char
                    ans = first_match and dp(i+1, j+1)

            memo[i, j] = ans

            return memo[i, j]

        return dp(0, 0)


if __name__ == "__main__":
    s = Solution()

    input_pair = ("aa", "a*a")
    result = s.isMatch(*input_pair)

    print(result)

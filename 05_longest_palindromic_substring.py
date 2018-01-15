def expand_iter(s, spos, epos, slen):
    # print(s, spos, epos, slen)
    if spos == 0:
        return None

    end_limit = min((slen - epos - 1, spos)) + 1
    result = ""

    for n in range(0, end_limit):
        if s[spos-n] == s[epos+n]:
            result = s[spos - n:epos + n+1]
            continue
        else:
            print(result)
            return result

    print(result)
    return result


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_len = 1
        max_pal = s[0]
        slen = len(s)

        print("-----1-----")
        for pos, char in enumerate(s):
            if max_len > slen - pos + 2:
                break

            pal = expand_iter(s, pos, pos, slen)
            if pal == None:
                continue

            pal_len = len(pal)

            if pal_len > max_len:
                max_pal = pal
                max_len = pal_len

        print("-----2-----")
        for pos, char in enumerate(s):
            if max_len > slen - pos + 1:
                break

            pal = expand_iter(s, pos, pos - 1, slen)
            if pal == None:
                continue

            pal_len = len(pal)

            if pal_len > max_len:
                max_pal = pal
                max_len = pal_len

        return max_pal


s = Solution()

# result = s.longestPalindrome("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
result = s.longestPalindrome("ababababa")

print("Result: %s" % result)


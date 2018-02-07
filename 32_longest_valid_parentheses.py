class Solution:
    def check_dup(self, _stack, new_val):
        if _stack:
            last_par = _stack[-1]

            if new_val < last_par[0]:
                _stack.pop()

                return self.check_dup(_stack, new_val)

        return _stack

    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """

        stack = list()
        par_stack = list()

        for pos, val in enumerate(s):
            if val == '(':  # open
                stack.append(pos)

            elif val == ')':  # close
                if not stack:
                    cont_len = 0
                    continue

                spos = stack.pop()

                par_stack = self.check_dup(par_stack, spos)

                par_stack.append((spos, pos))

        last_epos = -1
        max_val = 0
        cont = 0

        for par in par_stack:
            spos = par[0]
            epos = par[1]

            par_len = epos - spos + 1

            if last_epos + 1 == spos:
                cont += par_len
            else:
                cont = par_len

            max_val = max(max_val, cont)

            last_epos = epos

        print(s, max_val, par_stack)

        return max_val


s = Solution()

_input = "(()"

r = s.longestValidParentheses("(())()(()((")
r = s.longestValidParentheses(_input)
r = s.longestValidParentheses("()()")
r = s.longestValidParentheses(")()(((())))(")
r = s.longestValidParentheses("(()())")
r = s.longestValidParentheses("((()))())")
r = s.longestValidParentheses("(()()(())((")
r = s.longestValidParentheses(")()())()()(")
r = s.longestValidParentheses(")(())(()()))(")

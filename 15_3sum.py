class Solution:
    def threeSum(selfself, nums):
        nums = sorted(nums)
        
        result = list()
        lnum = len(nums) - 1

        for pos, n in enumerate(nums):

            if pos + 1 == lnum:
                break

            start = pos + 1
            end = lnum

            if pos > 0 and nums[pos - 1] == n:
                continue

            dupchk = list()

            while start < end:
                nstart = nums[start]
                nend = nums[end]

                nsum = n + nstart + nend

                if nsum > 0:
                    end -= 1
                elif nsum < 0:
                    start += 1
                else:
                    if nstart not in dupchk:
                        dupchk.append(nstart)
                        answer = [n, nstart, nend]
                        result.append(answer)
                    end -= 1
                    start += 1

        return result


s = Solution()

# nums = [-10,-11,13,0,-11,9,1,-6,-1,-12,10,-9,0,-15,-13,4,-13,
#         -1,-12,2,-11,-6,10,2,-6,6,-8,-12,11,-2,1,9,2,-1,-14,
#         -1,-6,-6,0,0,-3,-4,-2,4,-12,-8,-7,-10,6,-11,-1,2,-2,
#         -14,-10,7,7,-3,10,-4,3,-11,-10,12,3,13,-4,4,-8,4,-11,
#         -4,-15,-6,-15,-12,1,-15,-15,14,-11,-8,2,-6,-7,-1,-14,
#         -14,11,4,-3,-1,8,-6,-3,-12,-8,0,8,-1,11,4,2,11,14,2,
#         6,-8,-6,-1,-8,-1,6]

nums = [-2,0,0,2,2]

result = s.threeSum(nums)

print(result)

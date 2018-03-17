class Solution:
    def __init__(self):
        self.result = list()

    def _permute(self, nums, result):
        lnums = len(nums)
        if lnums < 2:
            if lnums > 0:
                result.append(nums[0])
            self.result.append(result)
            return True

        for p, n in enumerate(nums):
            subnums = nums[:p] + nums[p + 1:]
            self._permute(subnums, result + [n])

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        for p, n in enumerate(nums):
            subnums = nums[:p] + nums[p+1:]
            self._permute(subnums, [n])

        return self.result

s = Solution()

result = s.permute([1])

print(result)

print(len(result))
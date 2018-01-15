class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        comb = list()

        n = len(nums1)
        m = len(nums2)

        tot = n + m
        med = (n + m) // 2 + 1

        cnt = 0

        while len(nums1) > 0 or len(nums2) > 0:
            if not nums1:
                comb = comb + nums2
                break

            if not nums2:
                comb = comb + nums1
                break

            if nums1[0] > nums2[0]:
                comb.append(nums2.pop(0))
            else:
                comb.append(nums1.pop(0))

            cnt += 1

            if cnt == med:
                if tot % 2 == 1:
                    return float(comb[med - 1])
                else:
                    left = comb[med - 2]
                    right = comb[med - 1]
                    print(left, right)
                    return (left + right) / 2


        print(comb)

        lcomb = len(comb)

        if lcomb % 2 == 1:
            return float(comb[lcomb // 2])
        else:
            left = comb[lcomb // 2 - 1]
            right = comb[lcomb // 2]
            return (left + right) / 2




s = Solution()

num1 = [1, 2, 4, 6, 22, 24]
num2 = [2, 3, 5, 11, 15]

med = s.findMedianSortedArrays(num1, num2)

print(med)

class Solution:
    def median(self, A, B):
        m, n = len(A), len(B)
        if m > n:
            A, B, m, n = B, A, n, m
        if n == 0:
            raise ValueError

        imin, imax, half_len = 0, m, (m + n + 1) // 2

        while imin <= imax:
            i = (imin + imax) // 2
            j = half_len - i

            if i < m and B[j - 1] > A[i]:
                # i is too small, must increase it
                imin = i + 1
            elif i > 0 and A[i - 1] > B[j]:
                # i is too big, must decrease it
                imax = i - 1
            else:
                # i is perfect

                if i == 0:
                    max_of_left = B[j - 1]
                elif j == 0:
                    max_of_left = A[i - 1]
                else:
                    max_of_left = max(A[i - 1], B[j - 1])

                if (m + n) % 2 == 1:
                    return max_of_left

                if i == m:
                    min_of_right = B[j]
                elif j == n:
                    min_of_right = A[i]
                else:
                    min_of_right = min(A[i], B[j])

                return (max_of_left + min_of_right) / 2.0

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

# num1 = [1, 2, 4, 6, 22, 24]
# num2 = [2, 3, 5, 11, 15]
#
# med1 = s.findMedianSortedArrays(num1, num2)

num1 = [1, 2, 4, 6, 22, 24]
num2 = [2, 3, 5, 11, 15]
med2 = s.median(num1, num2)

print(med2)

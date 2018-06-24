import sys

class Solution:

    # method 1 O(log(min(m,n))
    # **************************************************
    # TUT: https://www.youtube.com/watch?v=LPFhl65R7ww
    # **************************************************
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int] [1,4,5,8]    [2]
        :type nums2: List[int] [1,1,2,2,2]  [1,3]
        :rtype: float
        """
        x = len(nums1)
        y = len(nums2)

        if x > y:
            return self.findMedianSortedArrays(nums2, nums1)

        low = 0
        high = x
        while low <= high:
            cut_xi = int((high + low) / 2)
            cut_yi = int((x + y + 1) / 2) - cut_xi
            if cut_xi == 0:
                xl = - sys.maxsize
            else:
                xl = nums1[cut_xi - 1]

            if cut_xi == x:
                xr = sys.maxsize
            else:
                xr = nums1[cut_xi]

            if cut_yi == 0:
                yl = - sys.maxsize
            else:
                yl = nums2[cut_yi - 1]

            if cut_yi == y:
                yr = sys.maxsize
            else:
                yr = nums2[cut_yi]

            if (xl <= yr) and (yl <= xr):
                if (x + y) % 2 == 0:
                    return (max(xl, yl) + min(xr, yr)) / 2
                else:
                    return max(xl, yl)
            elif xl > yr:
                high = int((high + low) / 2) - 1
            else:
                low = int((high + low) / 2) + 1

        # return self.linearTime(nums1, nums2)

    # method 2
    def linearTime(self, nums1, nums2):
        m = (len(nums1) + len(nums2)) / 2
        i = j = 0
        c_n_p = None
        c_n = None

        while i < len(nums1) and j < len(nums2):
            if i + j <= m:
                if nums1[i] <= nums2[j]:
                    c_n_p = c_n
                    c_n = nums1[i]
                    i += 1
                    # print("num1: %d" % c_n)
                else:
                    c_n_p = c_n
                    c_n = nums2[j]
                    j += 1
                    # print("num2: %d" % c_n)
            else:
                break

        while i < len(nums1) and i + j <= m:
            c_n_p = c_n
            c_n = nums1[i]
            i += 1
            # print("num1: %d" % c_n)

        while j < len(nums2) and i + j <= m:
            c_n_p = c_n
            c_n = nums2[j]
            j += 1
            # print("num2: %d" % c_n)

        if (len(nums1) + len(nums2)) % 2 > 0:
            return c_n
        else:
            return (c_n + c_n_p) / 2

if __name__ == '__main__':
    A = [2]
    B = [1,3]
    sol = Solution()
    print(sol.findMedianSortedArrays(A,B))

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        full_list = nums1 + nums2
        full_list = sorted(full_list)
        l = len(full_list)
        if l % 2 == 0:
            a = full_list[int(l/2-1)]
            b = full_list[int(l/2)]
            return (a+b)/2
        else:
            return full_list[int((l-1)/2)]
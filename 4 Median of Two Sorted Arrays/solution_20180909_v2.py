class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        total_length = len(nums1) + len(nums2)
        target_array = []
        if total_length % 2 == 1:
            target_idx = int((total_length-1)/2)
        else:
            target_idx = int(total_length/2)
            
        while True:
            if len(nums1) > 0 and len(nums2) > 0:
                if nums1[0] > nums2[0]:
                    target_array.append(nums2[0])
                    del nums2[0]
                elif nums1[0] < nums2[0]:
                    target_array.append(nums1[0])
                    del nums1[0]
                else:
                    target_array.append(nums1[0])
                    target_array.append(nums2[0])
                    del nums1[0]
                    del nums2[0]
            elif len(nums1) == 0 and len(nums2) > 0:
                target_array.append(nums2[0])
                del nums2[0]
            elif len(nums1) > 0 and len(nums2) == 0:
                target_array.append(nums1[0])
                del nums1[0]
                
            if len(target_array) > target_idx:
                if total_length % 2 == 1:
                    return target_array[target_idx]
                else:
                    return (target_array[target_idx] + target_array[target_idx-1])/2
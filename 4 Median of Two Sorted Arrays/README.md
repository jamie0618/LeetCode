# Median of Two Sorted Arrays (Hard)

## Question
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5

## 2018 09 09
runtime beat 34.21%

想法:

兩個 list 合併成一個，直接調用 python 內建 sorted function 排序

再找出中位數即可
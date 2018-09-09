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

## v1 2018/09/09
runtime beat 34.21%

兩個 list 合併成一個，直接調用 python 內建 sorted function 排序

再找出中位數即可

## v2 2018/09/09
runtime beat 66.89%

performance提升不少，但code相對複雜一些

開一個array用來存排序過的數字

輪流從頭比較兩個array中的數字大小，把小的那個放入新開的array，直到中位數的index為止

缺點是要考慮比較多if/else，例如 [1,2] [3,4]這種一個array全都比另一個array大的情況

不過優點是不需要看過所有 m+n 個數字，只要看過一半即可
# Two Sum (Easy)

## Question
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,

return [0, 1].

## v1 2018/09/09
runtime beat 30.85%

從頭開始，對於每個數先以目標值減去該數，得到剩餘目標

接著判斷剩餘目標是否在 array 當中，如果有則 return




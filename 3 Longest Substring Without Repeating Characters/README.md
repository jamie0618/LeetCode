# Longest Substring Without Repeating Characters (Medium)

## Question
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"

Output: 3 

Explanation: The answer is "abc", which the length is 3.

Example 2:

Input: "bbbbb"

Output: 1

Explanation: The answer is "b", with the length of 1.

Example 3:

Input: "pwwkew"

Output: 3

Explanation: The answer is "wke", with the length of 3. 

             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

## 2018 09 09
runtime beat 58.00%

想法:

index 從頭開始，用 while 逐步增長字串長度

每多一個字就判斷該字是否已存在字串中

已存在 -> 計算字串長度並判斷要不要更新最大長度，接著把起始 index + 1 從頭開始

不存在 -> 字串增長一個字
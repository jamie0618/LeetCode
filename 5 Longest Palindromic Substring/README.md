# Longest Palindromic Substring (Medium)

## Question
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.

Example 2:

Input: "cbbd"

Output: "bb"

## v1 2018/09/10
runtime beat 46.33%

對於這種對稱形式的字串，首先我會分成兩種來處理

1. 奇數長度
	如: 'abxba'，中間的字元隨意，兩邊對稱
2. 偶數長度
	如: 'abxxba'，中間兩個字元相等，兩邊對稱
    
我用比較暴力的解法先處理邊界條件的情況

1. 字串長度=0: 回傳空字串
2. 字串長度=1: 回傳該字串
3. 字串長度=2: 如果兩個字一樣就回傳字串，不然就隨便挑一個字回傳

接著分成奇偶數處理，假設字串為'012345'，最外層的for迴圈會從index 1~4輪流當作中間的字元

然後逐步檢查前後兩個字元是否相等，如果相等，就繼續往外擴張檢查，不相等就停止

例子: 字串'cabaad'

for迴圈檢查 a b a a 四個字元

1. 奇數檢查:
	'a' -> 'cab' -> 因為 c!=b，停止
    
    'b' -> 'aba' -> 'cabad' -> 因為 c!=d，停止
    
    'a' -> 'baa' -> 因為 b!=a，停止
    
    'a' -> 'aad' -> 因為 a!=d，停止
    
2. 偶數檢查:
	'a' -> 判斷 a 和前後字元是否相等 -> 都不相等 -> 停止
    
    'b' -> 判斷 b 和前後字元是否相等 -> 都不相等 -> 停止
    
    'a' -> 判斷 a 和前後字元是否相等 -> 和後一個字元相等 -> 變成以'aa'為中心 -> 'baad' -> 因為 b!=d，停止
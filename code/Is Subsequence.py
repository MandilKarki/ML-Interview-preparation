'''
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the
characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde"
while "aec" is not).

Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false
'''


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)

''''
The code I provided checks if the first string (s) is a subsequence of the second string (t). It does this by iterating
through both strings using two pointers, one for each string.

The class Solution is defined and the function isSubsequence is defined which takes two parameters self and s,t.

The function starts by initializing two pointers, i and j, to 0. The variable i is used to keep track of the current 
position in the first string (s), while the variable j is used to keep track of the current position in the second string (t).

The while loop then iterates through both strings by comparing the characters at the current pointer positions. If the 
characters match, the pointer for the first string (s) is incremented. The pointer for the second string (t) is always 
incremented, regardless of whether the characters match.

The while loop continues until either the pointer for the first string (s) reaches the end of the string, or the pointer
for the second string (t) reaches the end of the string.

If the pointer for the first string (s) is at the end of the string, it means that all characters in the first string (s)
have been found in the second string (t) and the function returns true.
Otherwise, it returns false.

The function isSubsequence() uses a simple approach of two pointer technique to check if one string is a subsequence of 
the other. The time complexity of this algorithm is O(n) as we are iterating through both the strings once. The space
complexity is O(1) as we are not using any additional data structure.
'''
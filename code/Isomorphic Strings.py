'''
Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters.
No two characters may map to the same character, but a character may map to itself.

Example 1:
Input: s = "egg", t = "add"
Output: true

Example 2:
Input: s = "foo", t = "bar"
Output: false

Example 3:
Input: s = "paper", t = "title"
Output: true
'''


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_map = {}
        t_map = {}

        for i in range(len(s)):
            if s[i] not in s_map:
                s_map[s[i]] = t[i]
            else:
                if s_map[s[i]] != t[i]:
                    return False

            if t[i] not in t_map:
                t_map[t[i]] = s[i]
            else:
                if t_map[t[i]] != s[i]:
                    return False

        return True


'''
The code is checking if two strings, "s" and "t", are isomorphic, which means that they contain the same characters but
in possibly a different order. It does this by iterating through the characters of both strings and creating two dictionaries,
one for mapping characters in the first string to characters in the second string and the other for mapping characters 
in the second string to characters in the first string.

First it checks if the lengths of the two strings are different, if yes it returns False. This is because if the lengths
of the two strings are different, they cannot be isomorphic.

Then it creates two dictionaries, "s_map" and "t_map", which will store the mappings of characters from the first string
to the second string and from the second string to the first string respectively.

The code then iterates over the characters in both strings, for each character, it checks if it has already been mapped
in the corresponding dictionary. If it has, it checks if the mapping is consistent with the current character, if not it
returns False. This check is done to ensure that the same character in the first string maps to the same character in the
second string and vice versa.

If the character has not been mapped yet, it adds the mapping in the corresponding dictionary.

After the iteration, if all the mappings are consistent, it returns True, indicating that the two strings are isomorphic.
If at any point it returns False, it means that the strings are not isomorphic.

The overall the idea is to map characters of the first string to the characters of the second string in a one-to-one 
mapping, and check that the mapping is consistent throughout the string.
'''
class Solution(object):
    def maxFreqSum(self, s):
        unlilar = {'a', 'e', 'i', 'o', 'u'}
        u_count = {}
        u2_count = {}

        for i in s:
            if i in unlilar:
                u_count[i] = u_count.get(i, 0) + 1
            else:
                u2_count[i] = u2_count.get(i, 0) + 1

        max_vowel = max(u_count.values()) if u_count else 0
        max_consonant = max(u2_count.values()) if u2_count else 0

        return max_vowel + max_consonant
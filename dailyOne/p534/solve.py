"""
Given a string, determine if a permutation of the string could form a palindrome.

whether any PERMUTATION.
"""


# O(N) time and space.
def canPermutePalindrome(str):
    count = dict()
    for x in str:
        if x in count:
            count[x] += 1
        else:
            count[x] = 1
    odd = 0
    for x in count.values():
        if x % 2 != 0:
            odd += 1
    return odd <= 1

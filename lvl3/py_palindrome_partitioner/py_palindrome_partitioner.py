"""
Given a string `s`, find the minimum number of cuts needed
to partition it such that every resulting substring is a palindrome.

A cut divides the string between two characters. With `c` cuts,
the string is split into `c + 1` substrings. We want the minimum number
of cuts `c` such that all parts are palindromes.

Return this minimum number of cuts (an integer).

Constraints:
- An empty string or a string of length 1 is already a palindrome -> 0 cuts.
- If the entire string is already a palindrome -> 0 cuts.
- In the worst case (all characters are distinct), the result is len(s) - 1 cuts.
"""

def palindrome_partitioner(s: str) -> int:
    if s == s[::-1]:
        return 0
    best = len(s) - 1
    for i in range(1, len(s)):
        if s[:i] == s[:i][::-1]:
            best = min(best, 1 + palindrome_partitioner(s[i:]))
    return best


if __name__ == "__main__":
    print(palindrome_partitioner("aab"))
    # 1

    print(palindrome_partitioner("aba"))
    # 0

    print(palindrome_partitioner("abc"))
    # 2
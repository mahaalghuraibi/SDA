# -----------------------------------------------------------------
# Challenge: 16_almost_palindrome
# Prompt:
# Write a function called `almost_palindrome` that accepts a single string
# and returns True if the string is:
#   1) A palindrome (reads the same forwards and backwards), OR
#   2) Can become a palindrome by removing **at most one character**.
#
# Ignore case and non-alphanumeric characters.
#
# Example function calls:
# almost_palindrome("racecar")      # returns True (already a palindrome)
# almost_palindrome("abca")         # returns True (remove 'c' -> 'aba')
# almost_palindrome("hello")        # returns False
# almost_palindrome("A man, a plan, a canal, Panama")  # returns True
#
# Hints:
# - Use string preprocessing to remove non-alphanumeric characters and lowercase everything.
# - Consider two-pointer technique (start and end) to check for palindrome.
# -----------------------------------------------------------------

def almost_palindrome(s):
    s = "".join(ch.lower() for ch in s if ch.isalnum())
    left, right = 0, len(s) - 1

    def is_palindrome(l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    while left < right:
        if s[left] != s[right]:
            return is_palindrome(left+1, right) or is_palindrome(left, right-1)
        left += 1
        right -= 1

    return True


print(almost_palindrome("racecar"))
print(almost_palindrome("abca"))
print(almost_palindrome("hello"))
print(almost_palindrome("A man, a plan, a canal, Panama"))

# -----------------------------------------------------------------
# Challenge: 20_compress_string
# Prompt:
# Write a function called `compress_string` that takes a string as input
# and returns a "compressed" version of the string where consecutive
# repeated characters are replaced by the character followed by the count.
#
# Only compress if the count is greater than 1. Single characters remain unchanged.
#
# Examples:
# compress_string("aaabbc")  -> "a3b2c"
# compress_string("abcd")    -> "abcd"
# compress_string("wwwwaaadexxxxx") -> "w4a3dex5"
#
# Notes:
# - The input string may contain letters, digits, and symbols.
# - Case-sensitive: 'a' and 'A' are different characters.
# - Do not use any external libraries.
# -----------------------------------------------------------------

def compress_string(s):
    result = ""       
    count = 1          

    for i in range(1, len(s)):
        if s[i] == s[i-1]:       
            count += 1
        else:                     
            if count > 1:
                result += s[i-1] + str(count)
            else:
                result += s[i-1]
            count = 1             

    if count > 1:
        result += s[-1] + str(count)
    else:
        result += s[-1]

    return result


print(compress_string("aaabbc"))        
print(compress_string("abcd"))         
print(compress_string("wwwwaaadexxxxx")) 

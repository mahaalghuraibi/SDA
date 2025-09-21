# 1. Vowel Counter
def count_vowels(s: str) -> int:
    vowels = set("aeiou")
    s = s.lower()
    return sum(1 for char in s if char in vowels)


# 2. String Occurrences of 'bob'
def count_bob_occurrences(s: str) -> int:
    count = 0
    for i in range(len(s) - 2):
        if s[i:i+3] == "bob":
            count += 1
    return count


# 3. String Reversal
def reverse_string(s: str) -> str:
    return s[::-1]


# 4. Letter Case Counter
def count_case(s: str) -> tuple[int, int]:
    upper = sum(1 for char in s if char.isupper())
    lower = sum(1 for char in s if char.islower() or char == " ")
    return upper, lower


# 5. Alphabetical Sorting of Words
def sort_words(csv_words: str) -> str:
    words = [w.strip() for w in csv_words.split(",")]
    return ", ".join(sorted(words))


# 6. Palindrome Checker
def is_palindrome(s: str) -> bool:
    s = s.lower().replace(" ", "")
    return s == s[::-1]


print(count_vowels("azcbobobegghakl"))   # 5
print(count_bob_occurrences("azcbobobegghakl"))  # 2
print(reverse_string("Programming in Python"))  # nohtyP ni gnimmargorP
print(count_case("Hello World"))  # (2, 9)
print(sort_words("without, hello, bag, world"))  # bag, hello, without, world
print(is_palindrome("madam"))  # True
print(is_palindrome("maha"))   # False

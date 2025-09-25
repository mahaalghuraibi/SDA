# -----------------------------------------------------------------
# Challenge: 18_group_anagrams
# Prompt:
# Write a function called `group_anagrams` that accepts a list of strings
# and returns a list of lists, where each sublist contains words that are
# anagrams of each other.
#
# Example function call:
# group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
#
# Expected output:
# [
#   ["eat", "tea", "ate"],
#   ["tan", "nat"],
#   ["bat"]
# ]
#
# Notes:
# - The order of the groups or the order of words inside each group does not matter.
# - Consider using a dictionary to group words by a key representing their letters.
# - Hint: Sorting the characters in a word can help identify anagrams.
# -----------------------------------------------------------------

def group_anagrams(words):
    groups = {}
    for word in words:
        key = "".join(sorted(word))
        if key not in groups:
            groups[key] = []
        groups[key].append(word)
    return list(groups.values())


if __name__ == "__main__":
    print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
